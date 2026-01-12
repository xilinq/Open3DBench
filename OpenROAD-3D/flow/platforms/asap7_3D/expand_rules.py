#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import re
from pathlib import Path


# base metal block is identified by: "Metal <m> RESOVER" (no extra index)
BASE_START_RE = re.compile(r"^\s*Metal\s+(\d+)\s+RESOVER\s*$")
LAYERCOUNT_RE = re.compile(r"^\s*LayerCount\s+\d+\s*$")
END_DENSITYMODEL_RE = re.compile(r"^\s*END\s+DensityModel\b")
WIDTH_LINE_RE = re.compile(r"^\s*WIDTH\s+Table\s+\d+\s+entries:\s*(.*)\s*$")

# section headers (no trailing index/targets)
SECTION_HEADER_RE = re.compile(r"^\s*Metal\s+(\d+)\s+(RESOVER|OVER|UNDER|DIAGUNDER|OVERUNDER)\s*$")

# coupling / subblock headers
RESOVER_IDX_RE = re.compile(r"^\s*Metal\s+(\d+)\s+RESOVER\s+(\d+)\s*$")
OVER_T_RE = re.compile(r"^\s*Metal\s+(\d+)\s+OVER\s+(\d+)\s*$")
UNDER_T_RE = re.compile(r"^\s*Metal\s+(\d+)\s+UNDER\s+(\d+)\s*$")
DIAGUNDER_T_RE = re.compile(r"^\s*Metal\s+(\d+)\s+DIAGUNDER\s+(\d+)\s*$")
OVERUNDER_RE = re.compile(r"^\s*Metal\s+(\d+)\s+OVER\s+(\d+)\s+UNDER\s+(\d+)\s*$")


def _parse_first_float(s: str) -> float | None:
    # width line may contain multiple numbers; we only need the first.
    m = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", s)
    if not m:
        return None
    try:
        return float(m.group(0))
    except ValueError:
        return None


def split_header_and_metal_blocks(lines: list[str]) -> tuple[list[str], dict[int, list[str]], list[str]]:
    """
    Returns: (header_lines_before_first_base, {metal: base_block_lines}, tail_lines_from_END_DensityModel_inclusive)
    """
    end_idx = None
    for i, ln in enumerate(lines):
        if END_DENSITYMODEL_RE.match(ln):
            end_idx = i
            break
    if end_idx is None:
        raise ValueError("未找到 'END DensityModel' 行。")

    tail = lines[end_idx:]  # include END DensityModel and anything after
    body = lines[:end_idx]

    # locate base starts
    base_starts: list[tuple[int, int]] = []  # (index, metal)
    for i, ln in enumerate(body):
        m = BASE_START_RE.match(ln)
        if m:
            base_starts.append((i, int(m.group(1))))

    if not base_starts:
        raise ValueError("未找到任何 'Metal <n> RESOVER' 基础块起始行。")

    header = body[: base_starts[0][0]]

    blocks: dict[int, list[str]] = {}
    for idx, (start_i, metal) in enumerate(base_starts):
        end_i = base_starts[idx + 1][0] if idx + 1 < len(base_starts) else len(body)
        blocks[metal] = body[start_i:end_i]

    return header, blocks, tail


def get_section_width(block: list[str], metal: int, section: str) -> float:
    """
    Find width from:
      Metal <metal> <section>
      WIDTH Table ...
    If not found / not parseable => 0.0
    """
    header_re = re.compile(rf"^\s*Metal\s+{metal}\s+{re.escape(section)}\s*$")
    for i, ln in enumerate(block):
        if header_re.match(ln):
            # search forward for WIDTH line
            for j in range(i + 1, min(i + 6, len(block))):
                m = WIDTH_LINE_RE.match(block[j])
                if m:
                    w = _parse_first_float(m.group(1))
                    return 0.0 if w is None else w
            return 0.0
    return 0.0


def extract_subblocks(block: list[str], metal: int) -> dict[tuple, list[str]]:
    """
    Extract subblocks keyed by:
      ("RESOVER", idx)
      ("OVER", t)
      ("UNDER", t)
      ("DIAGUNDER", t)
      ("OVERUNDER", over, under)
    Subblock lines include header + DIST..END DIST (and may include blank lines after END DIST in source;
    we normalize when emitting).
    """
    out: dict[tuple, list[str]] = {}

    i = 0
    n = len(block)
    while i < n:
        ln = block[i]

        key: tuple | None = None
        m = RESOVER_IDX_RE.match(ln)
        if m and int(m.group(1)) == metal:
            key = ("RESOVER", int(m.group(2)))
        else:
            m = OVER_T_RE.match(ln)
            if m and int(m.group(1)) == metal:
                key = ("OVER", int(m.group(2)))
            else:
                m = UNDER_T_RE.match(ln)
                if m and int(m.group(1)) == metal:
                    key = ("UNDER", int(m.group(2)))
                else:
                    m = DIAGUNDER_T_RE.match(ln)
                    if m and int(m.group(1)) == metal:
                        key = ("DIAGUNDER", int(m.group(2)))
                    else:
                        m = OVERUNDER_RE.match(ln)
                        if m and int(m.group(1)) == metal:
                            key = ("OVERUNDER", int(m.group(2)), int(m.group(3)))

        if key is None:
            i += 1
            continue

        # capture until END DIST
        j = i
        while j < n and block[j].strip() != "END DIST":
            j += 1
        if j >= n:
            # malformed; bail out by not capturing
            i += 1
            continue

        # include END DIST line
        j_end = j + 1
        out[key] = block[i:j_end]
        i = j_end

    return out


def collect_existing_keys(block: list[str], metal: int) -> set[tuple]:
    """
    Keys:
      ("RESOVER", idx)
      ("OVER", t)
      ("UNDER", t)
      ("DIAGUNDER", t)
      ("OVERUNDER", over, under)
    """
    keys: set[tuple] = set()
    for ln in block:
        m = RESOVER_IDX_RE.match(ln)
        if m and int(m.group(1)) == metal:
            keys.add(("RESOVER", int(m.group(2))))
            continue
        m = OVER_T_RE.match(ln)
        if m and int(m.group(1)) == metal:
            keys.add(("OVER", int(m.group(2))))
            continue
        m = UNDER_T_RE.match(ln)
        if m and int(m.group(1)) == metal:
            keys.add(("UNDER", int(m.group(2))))
            continue
        m = DIAGUNDER_T_RE.match(ln)
        if m and int(m.group(1)) == metal:
            keys.add(("DIAGUNDER", int(m.group(2))))
            continue
        m = OVERUNDER_RE.match(ln)
        if m and int(m.group(1)) == metal:
            keys.add(("OVERUNDER", int(m.group(2)), int(m.group(3))))
            continue
    return keys


def stub_dist_block(width: float) -> list[str]:
    # match existing style: "DIST count 0 width <w>" then "END DIST"
    w_str = "0" if width == 0.0 else f"{width:g}"
    return [f"DIST count 0 width {w_str}\n", "END DIST\n"]


def _normalize_subblock_lines(lines: list[str], new_header: str) -> list[str]:
    """
    Rewrite first line to new_header and normalize trailing blank lines.
    Always ends with a single blank line.
    """
    if not lines:
        return []

    out = list(lines)
    # force newline on header
    out[0] = new_header if new_header.endswith("\n") else (new_header + "\n")

    # ensure all lines end with '\n'
    for i in range(len(out)):
        if not out[i].endswith("\n"):
            out[i] += "\n"

    # drop trailing blank lines
    while out and out[-1].strip() == "":
        out.pop()

    out.append("\n")
    return out


def mirror_index(x: int, layercount: int) -> int:
    # 1<->layercount, 2<->layercount-1 ...
    return (layercount + 1) - x


def build_mirrored_upper_metal_block(
    target_m: int,
    layercount: int,
    split: int,
    source_widths: dict[int, dict[str, float]],
    source_subblocks: dict[int, dict[tuple, list[str]]],
) -> list[str]:
    """
    Build Metal target_m block (target_m in split+1..layercount) by mirroring data from 1..split.
    Cross-half couplings are left empty (stubs).

    Mapping required by user:
      7->8, 6->9, ..., 1->14  (when layercount=14 and split=7)
    Which is exactly mirror_index(x, 14) = 15-x.
    """
    if not (split + 1 <= target_m <= layercount):
        raise ValueError("build_mirrored_upper_metal_block only supports upper-half metals")

    src_self = mirror_index(target_m, layercount)  # e.g. 8->7, 14->1
    w = source_widths.get(src_self, {})

    w_res = w.get("RESOVER", 0.0)
    w_over = w.get("OVER", 0.0)
    w_under = w.get("UNDER", 0.0)
    w_diag = w.get("DIAGUNDER", 0.0)
    w_ou = w.get("OVERUNDER", 0.0)

    src_self_blocks = source_subblocks.get(src_self, {})

    def maybe_fill_resover_idx(idx: int) -> list[str] | None:
        # 只镜像拷贝 idx=0 的非空数据；其他 idx 仍保持为空
        if idx != 0:
            return None
        sb = src_self_blocks.get(("RESOVER", 0))
        if not sb:
            return None
        return _normalize_subblock_lines(sb, f"Metal {target_m} RESOVER 0")

    def maybe_fill_over(k: int) -> list[str] | None:
        # OVER 0: 直接拷贝同层的 OVER 0
        if k == 0:
            sb = src_self_blocks.get(("OVER", 0))
            if not sb:
                return None
            return _normalize_subblock_lines(sb, f"Metal {target_m} OVER 0")

        # 仅填“上半区内部”的 OVER（k in 8..target_m-1），跨半区(1..7)保持空
        if k < (split + 1):
            return None
        if not (split + 1 <= k <= target_m - 1):
            return None

        # target: Metal target_m OVER k
        # source pair: (src_self UNDER src_k) where src_k = mirror_index(k)
        src_k = mirror_index(k, layercount)  # in 1..split
        sb = src_self_blocks.get(("UNDER", src_k))
        if not sb:
            return None
        return _normalize_subblock_lines(sb, f"Metal {target_m} OVER {k}")

    def maybe_fill_under(u: int) -> list[str] | None:
        # 仅填“上半区内部”的 UNDER（u in target_m+1..14 且 u>=8），跨半区无
        if u < (split + 1):
            return None
        if not (target_m + 1 <= u <= layercount):
            return None

        # target: Metal target_m UNDER u
        # source: Metal src_self OVER src_u where src_u = mirror_index(u)
        src_u = mirror_index(u, layercount)  # in 1..split, and src_u < src_self
        sb = src_self_blocks.get(("OVER", src_u))
        if not sb:
            return None
        return _normalize_subblock_lines(sb, f"Metal {target_m} UNDER {u}")

    def maybe_fill_diagunder(u: int) -> list[str] | None:
        # 仅填“上半区内部”的 DIAGUNDER（u>=8）
        if u < (split + 1):
            return None
        if not (target_m + 1 <= u <= layercount):
            return None

        # target: Metal target_m DIAGUNDER u
        # source: Metal src_base DIAGUNDER src_self
        src_base = mirror_index(u, layercount)  # in 1..split (lower in original)
        sb = source_subblocks.get(src_base, {}).get(("DIAGUNDER", src_self))
        if not sb:
            return None
        return _normalize_subblock_lines(sb, f"Metal {target_m} DIAGUNDER {u}")

    def maybe_fill_overunder(over: int, under: int) -> list[str] | None:
        # 仅填“上半区内部”的 OVERUNDER (over>=8 and under>=8)
        if over < (split + 1) or under < (split + 1):
            return None
        if not (1 <= over <= target_m - 1):
            return None
        if not (target_m + 1 <= under <= layercount):
            return None

        # target: Metal target_m OVER over UNDER under
        # source: Metal src_self OVER src_over UNDER src_under
        # where src_over = mirror(under), src_under = mirror(over)
        src_over = mirror_index(under, layercount)  # below src_self
        src_under = mirror_index(over, layercount)  # above src_self
        sb = src_self_blocks.get(("OVERUNDER", src_over, src_under))
        if not sb:
            return None
        return _normalize_subblock_lines(sb, f"Metal {target_m} OVER {over} UNDER {under}")

    out: list[str] = []

    # RESOVER
    out.append(f"Metal {target_m} RESOVER\n")
    out.append(f"WIDTH Table 1 entries:  {w_res:g}\n\n")
    for idx in range(0, target_m):  # 0..m-1
        filled = maybe_fill_resover_idx(idx)
        if filled is not None:
            out.extend(filled)
        else:
            out.append(f"Metal {target_m} RESOVER {idx}\n")
            out.extend(stub_dist_block(w_res))
            out.append("\n")

    # OVER
    out.append(f"Metal {target_m} OVER\n")
    out.append(f"WIDTH Table 1 entries:  {w_over:g}\n\n")
    for k in range(0, target_m):  # 0..m-1
        filled = maybe_fill_over(k)
        if filled is not None:
            out.extend(filled)
        else:
            out.append(f"Metal {target_m} OVER {k}\n")
            out.extend(stub_dist_block(w_over))
            out.append("\n")

    # UNDER
    out.append(f"Metal {target_m} UNDER\n")
    out.append(f"WIDTH Table 1 entries:  {w_under:g}\n\n")
    for u in range(target_m + 1, layercount + 1):
        filled = maybe_fill_under(u)
        if filled is not None:
            out.extend(filled)
        else:
            out.append(f"Metal {target_m} UNDER {u}\n")
            out.extend(stub_dist_block(w_under))
            out.append("\n")

    # DIAGUNDER
    out.append(f"Metal {target_m} DIAGUNDER\n")
    out.append(f"WIDTH Table 1 entries:  {w_diag:g}\n\n")
    for u in range(target_m + 1, layercount + 1):
        filled = maybe_fill_diagunder(u)
        if filled is not None:
            out.extend(filled)
        else:
            out.append(f"Metal {target_m} DIAGUNDER {u}\n")
            out.extend(stub_dist_block(w_diag))
            out.append("\n")

    # OVERUNDER
    out.append(f"Metal {target_m} OVERUNDER\n")
    out.append(f"WIDTH Table 1 entries:  {w_ou:g}\n\n")
    for over in range(1, target_m):
        for under in range(target_m + 1, layercount + 1):
            filled = maybe_fill_overunder(over, under)
            if filled is not None:
                out.extend(filled)
            else:
                out.append(f"Metal {target_m} OVER {over} UNDER {under}\n")
                out.extend(stub_dist_block(w_ou))
                out.append("\n")

    return out


def build_canonical_metal_block_from_existing(existing_block: list[str], metal: int, layercount: int) -> list[str]:
    """
    Re-emit a metal block in canonical order:
      RESOVER -> OVER -> UNDER -> DIAGUNDER -> OVERUNDER
    After each section header+WIDTH, emit ALL required subblocks (even empty stubs).
    Existing subblocks (where present) are reused (header rewritten), otherwise stubbed.
    """
    if not existing_block:
        return []

    # widths from existing headers (if missing -> 0.0)
    w_res = get_section_width(existing_block, metal, "RESOVER")
    w_over = get_section_width(existing_block, metal, "OVER")
    w_under = get_section_width(existing_block, metal, "UNDER")
    w_diag = get_section_width(existing_block, metal, "DIAGUNDER")
    w_ou = get_section_width(existing_block, metal, "OVERUNDER")

    subs = extract_subblocks(existing_block, metal)

    out: list[str] = []

    # RESOVER
    out.append(f"Metal {metal} RESOVER\n")
    out.append(f"WIDTH Table 1 entries:  {w_res:g}\n\n")
    for idx in range(0, metal):
        key = ("RESOVER", idx)
        sb = subs.get(key)
        if sb:
            out.extend(_normalize_subblock_lines(sb, f"Metal {metal} RESOVER {idx}"))
        else:
            out.append(f"Metal {metal} RESOVER {idx}\n")
            out.extend(stub_dist_block(w_res))
            out.append("\n")

    # OVER
    out.append(f"Metal {metal} OVER\n")
    out.append(f"WIDTH Table 1 entries:  {w_over:g}\n\n")
    for t in range(0, metal):
        key = ("OVER", t)
        sb = subs.get(key)
        if sb:
            out.extend(_normalize_subblock_lines(sb, f"Metal {metal} OVER {t}"))
        else:
            out.append(f"Metal {metal} OVER {t}\n")
            out.extend(stub_dist_block(w_over))
            out.append("\n")

    # UNDER
    out.append(f"Metal {metal} UNDER\n")
    out.append(f"WIDTH Table 1 entries:  {w_under:g}\n\n")
    for t in range(metal + 1, layercount + 1):
        key = ("UNDER", t)
        sb = subs.get(key)
        if sb:
            out.extend(_normalize_subblock_lines(sb, f"Metal {metal} UNDER {t}"))
        else:
            out.append(f"Metal {metal} UNDER {t}\n")
            out.extend(stub_dist_block(w_under))
            out.append("\n")

    # DIAGUNDER
    out.append(f"Metal {metal} DIAGUNDER\n")
    out.append(f"WIDTH Table 1 entries:  {w_diag:g}\n\n")
    for t in range(metal + 1, layercount + 1):
        key = ("DIAGUNDER", t)
        sb = subs.get(key)
        if sb:
            out.extend(_normalize_subblock_lines(sb, f"Metal {metal} DIAGUNDER {t}"))
        else:
            out.append(f"Metal {metal} DIAGUNDER {t}\n")
            out.extend(stub_dist_block(w_diag))
            out.append("\n")

    # OVERUNDER
    out.append(f"Metal {metal} OVERUNDER\n")
    out.append(f"WIDTH Table 1 entries:  {w_ou:g}\n\n")
    for over in range(1, metal):
        for under in range(metal + 1, layercount + 1):
            key = ("OVERUNDER", over, under)
            sb = subs.get(key)
            if sb:
                out.extend(_normalize_subblock_lines(sb, f"Metal {metal} OVER {over} UNDER {under}"))
            else:
                out.append(f"Metal {metal} OVER {over} UNDER {under}\n")
                out.extend(stub_dist_block(w_ou))
                out.append("\n")

    return out


def ensure_metal_block_complete(
    existing_block: list[str] | None,
    metal: int,
    layercount: int,
    preserve_existing: bool,
    *,
    mirror_lower_to_upper: bool = False,
    preserve_until: int = 7,
    source_widths: dict[int, dict[str, float]] | None = None,
    source_subblocks: dict[int, dict[tuple, list[str]]] | None = None,
) -> list[str]:
    """
    If preserve_existing=True: keep original lines, only append missing stubs.
    If preserve_existing=False:
      - if mirror_lower_to_upper and metal > preserve_until: generate a full skeleton and mirror-fill from 1..preserve_until
      - else: generate a fresh skeleton with empty stubs
    """
    if not preserve_existing:
        if mirror_lower_to_upper and metal > preserve_until:
            if source_widths is None or source_subblocks is None:
                raise ValueError("mirror_lower_to_upper requires source_widths/source_subblocks")
            return build_mirrored_upper_metal_block(
                target_m=metal,
                layercount=layercount,
                split=preserve_until,
                source_widths=source_widths,
                source_subblocks=source_subblocks,
            )

        # old behavior: fresh skeleton (all stubs, width=0.0)
        w = 0.0
        out: list[str] = []
        out.append(f"Metal {metal} RESOVER\n")
        out.append(f"WIDTH Table 1 entries:  {w:g}\n\n")
        for idx in range(0, metal):  # 0..metal-1
            out.append(f"Metal {metal} RESOVER {idx}\n")
            out.extend(stub_dist_block(w))
            out.append("\n")

        out.append(f"Metal {metal} OVER\n")
        out.append(f"WIDTH Table 1 entries:  {w:g}\n\n")
        for t in range(0, metal):  # 0..metal-1 (includes 0)
            out.append(f"Metal {metal} OVER {t}\n")
            out.extend(stub_dist_block(w))
            out.append("\n")

        out.append(f"Metal {metal} UNDER\n")
        out.append(f"WIDTH Table 1 entries:  {w:g}\n\n")
        for t in range(metal + 1, layercount + 1):
            out.append(f"Metal {metal} UNDER {t}\n")
            out.extend(stub_dist_block(w))
            out.append("\n")

        out.append(f"Metal {metal} DIAGUNDER\n")
        out.append(f"WIDTH Table 1 entries:  {w:g}\n\n")
        for t in range(metal + 1, layercount + 1):
            out.append(f"Metal {metal} DIAGUNDER {t}\n")
            out.extend(stub_dist_block(w))
            out.append("\n")

        out.append(f"Metal {metal} OVERUNDER\n")
        out.append(f"WIDTH Table 1 entries:  {w:g}\n\n")
        for over in range(1, metal):  # 1..metal-1 (no 0)
            for under in range(metal + 1, layercount + 1):
                out.append(f"Metal {metal} OVER {over} UNDER {under}\n")
                out.extend(stub_dist_block(w))
                out.append("\n")

        return out

    # preserve existing (Metal 1..preserve_until): append missing combinations as empty stubs
    if existing_block is None:
        return []
    return build_canonical_metal_block_from_existing(existing_block, metal, layercount)


def rewrite_layercount(header: list[str], layercount: int) -> list[str]:
    out: list[str] = []
    replaced = False
    for ln in header:
        if LAYERCOUNT_RE.match(ln):
            out.append(f"LayerCount {layercount}\n")
            replaced = True
        else:
            out.append(ln)
    if not replaced:
        inserted = False
        for i, ln in enumerate(out):
            if ln.strip().startswith("DIAGMODEL"):
                out.insert(i + 1, "\n")
                out.insert(i + 2, f"LayerCount {layercount}\n")
                inserted = True
                break
        if not inserted:
            out.append(f"LayerCount {layercount}\n")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Expand asap7_3D.rules to LayerCount=14 and ensure ALL coupling combinations exist; optionally mirror-fill upper metals from lower metals."
    )
    ap.add_argument("--input", default="asap7_3D.rules")
    ap.add_argument("--output", default="asap7_3D.rules")
    ap.add_argument("--layercount", type=int, default=14)
    ap.add_argument("--preserve-until", type=int, default=7, help="Preserve Metal 1..N content; N defaults to 7")
    ap.add_argument(
        "--mirror-lower-to-upper",
        action="store_true",
        help="Mirror-copy Metal 1..N data into Metal (N+1)..LayerCount (e.g. 7->8 ... 1->14), keep cross-half couplings empty.",
    )
    args = ap.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    lines = in_path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    header, blocks, tail = split_header_and_metal_blocks(lines)

    header = rewrite_layercount(header, args.layercount)

    # Prepare source data (for mirror)
    source_widths: dict[int, dict[str, float]] = {}
    source_subblocks: dict[int, dict[tuple, list[str]]] = {}
    if args.mirror_lower_to_upper:
        for m in range(1, args.preserve_until + 1):
            blk = blocks.get(m, [])
            source_widths[m] = {
                "RESOVER": get_section_width(blk, m, "RESOVER"),
                "OVER": get_section_width(blk, m, "OVER"),
                "UNDER": get_section_width(blk, m, "UNDER"),
                "DIAGUNDER": get_section_width(blk, m, "DIAGUNDER"),
                "OVERUNDER": get_section_width(blk, m, "OVERUNDER"),
            }
            source_subblocks[m] = extract_subblocks(blk, m)

    new_body: list[str] = []
    for m in range(1, args.layercount + 1):
        preserve = m <= args.preserve_until
        new_block = ensure_metal_block_complete(
            existing_block=blocks.get(m),
            metal=m,
            layercount=args.layercount,
            preserve_existing=preserve,
            mirror_lower_to_upper=args.mirror_lower_to_upper,
            preserve_until=args.preserve_until,
            source_widths=source_widths if args.mirror_lower_to_upper else None,
            source_subblocks=source_subblocks if args.mirror_lower_to_upper else None,
        )
        if not new_block:
            continue

        if new_body and (not new_body[-1].endswith("\n")):
            new_body[-1] += "\n"
        if new_body and new_body[-1].strip() != "":
            new_body.append("\n")
        new_body.extend(new_block)
        if new_body and new_body[-1].strip() != "":
            new_body.append("\n")

    out_lines = header + new_body + tail
    out_path.write_text("".join(out_lines), encoding="utf-8")
    print(
        f"Wrote {out_path} (LayerCount={args.layercount}, preserved Metal 1..{args.preserve_until}, "
        f"mirror_lower_to_upper={args.mirror_lower_to_upper})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())