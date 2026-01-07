#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


_RE_OBS_START = re.compile(r"^(\s*)OBS\s*$")
_RE_OBS_END = re.compile(r"^(\s*)END\s*$")
_RE_LAYER = re.compile(r"^(\s*)LAYER\s+(\S+)\s*;\s*$")


def reduce_obs(lef_text: str, default_layer: str = "M1") -> str:
	lines = lef_text.splitlines(keepends=True)
	out: list[str] = []

	in_obs = False
	obs_indent = ""
	first_layer_name: str | None = None

	for line in lines:
		if not in_obs:
			m = _RE_OBS_START.match(line.rstrip("\n\r"))
			if m:
				in_obs = True
				obs_indent = m.group(1)
				first_layer_name = None
				# 延迟输出，等读到 END 时再输出重写后的最小 OBS
				continue

			out.append(line)
			continue

		# in OBS
		ml = _RE_LAYER.match(line.rstrip("\n\r"))
		if ml and first_layer_name is None:
			first_layer_name = ml.group(2)
			continue

		me = _RE_OBS_END.match(line.rstrip("\n\r"))
		if me:
			layer = first_layer_name or default_layer

			# 复用 OBS 缩进风格：OBS 行缩进 + 两级缩进输出 LAYER/RECT
			layer_indent = obs_indent + "  "
			rect_indent = layer_indent + "  "

			out.append(f"{obs_indent}OBS\n")
			out.append(f"{layer_indent}LAYER {layer} ;\n")
			out.append(f"{rect_indent}RECT 0 0 0 0 ;\n")
			out.append(f"{obs_indent}END\n")

			in_obs = False
			obs_indent = ""
			first_layer_name = None
			continue

		# 其它 OBS 内行全部丢弃（包含所有 RECT / 额外 LAYER / V13/M12 等）
		continue

	return "".join(out)


def main() -> int:
	ap = argparse.ArgumentParser(
		description="Replace every OBS block in a LEF with a minimal OBS containing only 'RECT 0 0 0 0 ;'."
	)
	ap.add_argument(
		"--lef",
		type=Path,
		default=Path(__file__).with_name("asap7_bottom.lef"),
		help="Input LEF path (default: asap7_upper.lef next to this script).",
	)
	ap.add_argument("--out", type=Path, default=None, help="Output path (default: stdout unless --inplace).")
	ap.add_argument("--inplace", action="store_true", help="Overwrite input LEF in-place.")
	ap.add_argument("--default-layer", default="M2", help="Used when an OBS has no LAYER line (default: M2).")
	args = ap.parse_args()

	lef_path: Path = args.lef
	text = lef_path.read_text(encoding="utf-8", errors="replace")
	new_text = reduce_obs(text, default_layer=args.default_layer)

	if args.inplace:
		lef_path.write_text(new_text, encoding="utf-8")
		return 0

	if args.out is not None:
		args.out.write_text(new_text, encoding="utf-8")
		return 0

	# stdout
	import sys

	sys.stdout.write(new_text)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
