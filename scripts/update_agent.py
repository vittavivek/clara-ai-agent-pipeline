import json
import sys

v1_file = sys.argv[1]
update_file = sys.argv[2]

with open(v1_file) as f:
    memo = json.load(f)

with open(update_file) as f:
    update = json.load(f)

# apply updates
for key in update:
    memo[key] = update[key]

memo["version"] = "v2"

print(json.dumps(memo, indent=2))