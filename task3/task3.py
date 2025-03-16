import json
import sys


def update(d):
    if "value" in d:
        d["value"] = dct[d["id"]]
    if "values" in d:
        for v in d["values"]:
            update(v)


n = sys.argv[1]
m = sys.argv[2]
z = sys.argv[3]
value = json.load(open(n))
test = json.load(open(m))
dct = {}
for el in value["values"]:
    dct[el["id"]] = el["value"]
for el in test["tests"]:
    update(el)
with open(z, "w") as outfile:
    outfile.write(json.dumps(test, indent = 2))
