#!/usr/bin/env python3
"""
Transform a standard cell LEF into a "transparent" FEOL LEF by ensuring
each MACRO has an OBS with LAYER OVERLAP and a zero-area rectangle:

  OBS
    LAYER OVERLAP ;
      RECT 0 0 0 0 ;
  END

If a MACRO lacks an OBS block, one will be inserted just before the
"END <macroName>" line. If an OBS exists but lacks OVERLAP geometry,
it will be added at the top of that OBS block. Existing content is preserved.

Usage:
  python3 make_transparent_lef.py <input_lef> <output_lef>
If no arguments are provided, defaults to:
  input:  asap7sc7p5t_28_L.lef
  output: asap7sc7p5t_28_L_transparent.lef
"""

import sys
from pathlib import Path


def leading_spaces(s: str) -> str:
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    return s[:i]


def process_lef(lines):
    out = []
    inside_macro = False
    macro_name = None
    macro_had_obs = False
    inside_obs = False
    obs_buffer = []

    def flush_obs_buffer():
        nonlocal obs_buffer, macro_had_obs
        if not obs_buffer:
            return
        # Determine indentation from the 'OBS' line
        obs_indent = leading_spaces(obs_buffer[0])
        # Check if OVERLAP layer is already present
        has_overlap = any('LAYER' in l and 'OVERLAP' in l for l in obs_buffer)
        if not has_overlap:
            # Insert after the first line (the 'OBS' line)
            insertion = [
                f"{obs_indent}  LAYER OVERLAP ;\n",
                f"{obs_indent}    RECT 0 0 0 0 ;\n",
            ]
            obs_buffer = [obs_buffer[0]] + insertion + obs_buffer[1:]
        out.extend(obs_buffer)
        obs_buffer = []
        macro_had_obs = True

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not inside_macro:
            out.append(line)
            if stripped.startswith('MACRO '):
                inside_macro = True
                macro_had_obs = False
                parts = stripped.split()
                macro_name = parts[1] if len(parts) >= 2 else None
        else:
            # Inside a MACRO
            if inside_obs:
                obs_buffer.append(line)
                # OBS block ends with a bare 'END'
                if stripped == 'END':
                    flush_obs_buffer()
                    inside_obs = False
            else:
                # Not inside OBS
                if stripped == 'OBS':
                    inside_obs = True
                    obs_buffer = [line]
                else:
                    # Check for end of MACRO: 'END <macro_name>'
                    if stripped.startswith('END '):
                        # When encountering MACRO end, we might need to inject OBS
                        # Only if this 'END' actually closes the MACRO
                        # Some LEF writers put: END <pinName>, so confirm name
                        end_name = stripped[4:].strip()
                        if macro_name and end_name == macro_name:
                            if not macro_had_obs:
                                # Insert an OBS block before MACRO end
                                # Indentation aligns with other section keywords (two spaces)
                                out.append('  OBS\n')
                                out.append('    LAYER OVERLAP ;\n')
                                out.append('      RECT 0 0 0 0 ;\n')
                                out.append('  END\n')
                            out.append(line)
                            # Reset MACRO state
                            inside_macro = False
                            macro_name = None
                            macro_had_obs = False
                        else:
                            out.append(line)
                    else:
                        out.append(line)

        i += 1

    # If file ended while still inside an OBS (malformed), flush buffer to be safe
    if inside_obs and obs_buffer:
        flush_obs_buffer()
    return out


def main():
    # Defaults
    default_in = Path('asap7sc6t_26_L.lef')
    default_out = Path('asap7sc6t_26_L_transparent.lef')

    if len(sys.argv) >= 2:
        in_path = Path(sys.argv[1])
    else:
        in_path = default_in

    if len(sys.argv) >= 3:
        out_path = Path(sys.argv[2])
    else:
        out_path = default_out

    if not in_path.exists():
        sys.stderr.write(f"Input LEF not found: {in_path}\n")
        sys.exit(1)

    with in_path.open('r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    out_lines = process_lef(lines)

    with out_path.open('w', encoding='utf-8') as f:
        f.writelines(out_lines)

    print(f"Wrote transparent LEF to: {out_path}")


if __name__ == '__main__':
    main()
