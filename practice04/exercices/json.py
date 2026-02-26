import os
import sys

_this_dir = os.path.dirname(__file__)
_abs_this_dir = os.path.abspath(_this_dir)
sys.path = [p for p in sys.path if os.path.abspath(p) != _abs_this_dir]
import json as _json
sys.path.insert(0, _this_dir)


json_path = os.path.join(_this_dir, "json", "sample-data.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = _json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<60} {'Speed':<10} {'MTU':<5}")
print("-" * 80)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs.get("dn", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")
    print(f"{dn:<60} {speed:<10} {mtu:<5}")