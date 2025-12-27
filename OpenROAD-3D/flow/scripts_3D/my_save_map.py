import os
import pickle
import sys

def get_env(name: str, default=None, required=True):
    v = os.environ.get(name, default)
    if v is None and required:
        print(f"ERROR: {name} environment variable is not set.", file=sys.stderr)
    else:
        print(f"{name}: {v}")
    return v

design_dir    = get_env("DESIGN_DIR")
results_dir   = get_env("RESULTS_DIR")
def_version   = get_env("DEF_VERSION")
def_dimension = get_env("DESIGN_DIMENSION")

gp_out_file = f"{design_dir}{def_version}_{def_dimension}.gp.def"
name_die_map = {}
num_bot = num_upper = 0

with open(gp_out_file, "r", encoding="utf-8") as f:
    in_comps = False
    for line in f:
        ls = line.strip()
        if ls.startswith("COMPONENTS"):
            in_comps = True
            continue
        if ls.startswith("END COMPONENTS"):
            in_comps = False
            continue
        if not in_comps:
            continue
        # 组件行形如：- <cell_name> <class_name> + SOURCE ... + PLACED ...
        if ls.startswith("-"):
            parts = ls.split()
            if len(parts) >= 3:
                cell_name = parts[1]
                class_name = parts[2]
                cls_lower = class_name.lower()
                if "bottom" in cls_lower:
                    name_die_map[cell_name] = 0
                    num_bot += 1
                elif "upper" in cls_lower:
                    name_die_map[cell_name] = 1
                    num_upper += 1

os.makedirs(results_dir, exist_ok=True)
out_path = os.path.join(results_dir, "name_die_map.pkl")
with open(out_path, "wb") as pf:
    pickle.dump(name_die_map, pf)

print(f"Mapped bottom: {num_bot}, upper: {num_upper}, total: {len(name_die_map)}")
print(f"Saved to {out_path}")