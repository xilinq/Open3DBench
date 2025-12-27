#!/usr/bin/env python3
"""
Mirror metal (ROUTING) and via (CUT) layers from a 2D tech LEF to a
Face-to-Face top-die by duplicating LAYER, VIA, and VIARULE blocks with a
"_T" suffix, and remapping internal LAYER references accordingly.

Input:  asap7_tech_1x_201209.lef (same directory)
Output: asap7_tech_modified.lef   (same directory)
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple


THIS_DIR = Path(__file__).parent
INPUT_LEF = THIS_DIR / "asap7_tech_1x_201209.lef"
OUTPUT_LEF = THIS_DIR / "asap7_tech_modified.lef"


def read_lef_lines(path: Path) -> List[str]:
    return path.read_text(encoding="utf-8").splitlines(keepends=True)


def find_end_library_index(lines: List[str]) -> int:
    for idx, line in enumerate(lines):
        if line.strip() == "END LIBRARY":
            return idx
    raise RuntimeError("END LIBRARY not found in LEF file")


def collect_blocks(lines: List[str], start_regex: re.Pattern[str], end_name_from_header) -> List[List[str]]:
    blocks: List[List[str]] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if start_regex.match(line):
            header = line.rstrip("\n")
            end_name = end_name_from_header(header)
            block: List[str] = [lines[i]]
            i += 1
            # accumulate until END <name>
            while i < n:
                block.append(lines[i])
                if lines[i].strip() == f"END {end_name}":
                    i += 1
                    break
                i += 1
            blocks.append(block)
            continue
        i += 1
    return blocks


def layer_name_from_header(header: str) -> str:
    # header: "LAYER <name>"
    m = re.match(r"^\s*LAYER\s+(\S+)", header)
    if not m:
        raise ValueError(f"Invalid LAYER header: {header}")
    return m.group(1)


def via_name_from_header(header: str) -> str:
    # header: "VIA <name> ..." (keep rest as-is)
    m = re.match(r"^\s*VIA\s+(\S+)", header)
    if not m:
        raise ValueError(f"Invalid VIA header: {header}")
    return m.group(1)


def viarule_name_from_header(header: str) -> str:
    m = re.match(r"^\s*VIARULE\s+(\S+)", header)
    if not m:
        raise ValueError(f"Invalid VIARULE header: {header}")
    return m.group(1)


def layer_block_is_metal_or_cut(block: List[str]) -> Tuple[bool, str]:
    # Returns (keep, type_str)
    for line in block:
        m = re.search(r"\bTYPE\s+(MASTERSLICE|ROUTING|CUT)\b", line)
        if m:
            t = m.group(1)
            return (t in ("ROUTING", "CUT")), t
    return (False, "")


def mirror_layer_block(block: List[str]) -> List[str]:
    # rename header and end name with _T suffix; keep internals unchanged
    header = block[0].rstrip("\n")
    name = layer_name_from_header(header)
    mirrored: List[str] = []
    # header
    mirrored.append(re.sub(r"(^\s*LAYER\s+)\S+", r"\1" + name + "_T", block[0]))
    # body
    for line in block[1:-1]:
        mirrored.append(line)
    # end line
    end_line = block[-1]
    mirrored.append(end_line.replace(f"END {name}", f"END {name}_T"))
    return mirrored


def mirror_via_block(block: List[str]) -> List[str]:
    header = block[0].rstrip("\n")
    name = via_name_from_header(header)
    mirrored: List[str] = []
    # Replace the VIA name token, preserve the rest of the header line
    mirrored.append(re.sub(r"(^\s*VIA\s+)\S+", r"\1" + name + "_T", block[0]))
    # Map internal LAYER references to suffixed names
    layer_line_re = re.compile(r"^(\s*LAYER\s+)(\S+)(\s*;\s*)$")
    for line in block[1:-1]:
        m = layer_line_re.match(line)
        if m:
            mirrored.append(f"{m.group(1)}{m.group(2)}_T{m.group(3)}\n" if not line.endswith("\n") else f"{m.group(1)}{m.group(2)}_T{m.group(3)}")
        else:
            mirrored.append(line)
    # end line
    end_line = block[-1]
    mirrored.append(end_line.replace(f"END {name}", f"END {name}_T"))
    return mirrored


def mirror_viarule_block(block: List[str]) -> List[str]:
    header = block[0].rstrip("\n")
    name = viarule_name_from_header(header)
    mirrored: List[str] = []
    # Replace the VIARULE name token, preserve the rest
    mirrored.append(re.sub(r"(^\s*VIARULE\s+)\S+", r"\1" + name + "_T", block[0]))
    # Map internal LAYER references
    layer_line_re = re.compile(r"^(\s*LAYER\s+)(\S+)(\s*;\s*)$")
    for line in block[1:-1]:
        m = layer_line_re.match(line)
        if m:
            mirrored.append(f"{m.group(1)}{m.group(2)}_T{m.group(3)}\n" if not line.endswith("\n") else f"{m.group(1)}{m.group(2)}_T{m.group(3)}")
        else:
            mirrored.append(line)
    end_line = block[-1]
    mirrored.append(end_line.replace(f"END {name}", f"END {name}_T"))
    return mirrored


def generate_modified_lef() -> None:
    lines = read_lef_lines(INPUT_LEF)
    end_idx = find_end_library_index(lines)
    prefix = lines[:end_idx]  # exclude END LIBRARY

    # Collect blocks
    layer_blocks = collect_blocks(
        prefix,
        start_regex=re.compile(r"^\s*LAYER\s+\S+\s*$"),
        end_name_from_header=layer_name_from_header,
    )
    via_blocks = collect_blocks(
        prefix,
        start_regex=re.compile(r"^\s*VIA\s+\S+.*$"),
        end_name_from_header=via_name_from_header,
    )
    viarule_blocks = collect_blocks(
        prefix,
        start_regex=re.compile(r"^\s*VIARULE\s+\S+.*$"),
        end_name_from_header=viarule_name_from_header,
    )

    # Filter only ROUTING/CUT layers
    metal_or_cut_blocks: List[List[str]] = []
    for b in layer_blocks:
        keep, _t = layer_block_is_metal_or_cut(b)
        if keep:
            metal_or_cut_blocks.append(b)

    mirrored_layers: List[str] = []
    for b in metal_or_cut_blocks:
        mirrored_layers.extend(mirror_layer_block(b))

    mirrored_vias: List[str] = []
    for b in via_blocks:
        mirrored_vias.extend(mirror_via_block(b))

    mirrored_viarules: List[str] = []
    for b in viarule_blocks:
        mirrored_viarules.extend(mirror_viarule_block(b))

    out_lines: List[str] = []
    out_lines.extend(prefix)
    out_lines.append("\n# ----- Mirrored top-die (Face-to-Face) layers and vias -----\n")
    out_lines.extend(mirrored_layers)
    if mirrored_layers and not mirrored_layers[-1].endswith("\n"):
        out_lines.append("\n")
    out_lines.extend(mirrored_vias)
    if mirrored_vias and not mirrored_vias[-1].endswith("\n"):
        out_lines.append("\n")
    out_lines.extend(mirrored_viarules)
    if mirrored_viarules and not mirrored_viarules[-1].endswith("\n"):
        out_lines.append("\n")
    out_lines.append("END LIBRARY\n")

    OUTPUT_LEF.write_text("".join(out_lines), encoding="utf-8")


def main() -> None:
    generate_modified_lef()
    print(f"Generated: {OUTPUT_LEF}")


if __name__ == "__main__":
    main()



