import os, tempfile, json, csv
from edgeml_flow import core

def test_pipeline():
    d = tempfile.mkdtemp(); cp = os.path.join(d, "d.csv"); pp = os.path.join(d, "p.json")
    with open(cp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["x", "y"]); w.writeheader()
        for row in [{"x":"1","y":"2"},{"x":"3","y":"4"}]:
            w.writerow(row)
    json.dump({"steps":[{"op":"normalize","cols":["x"]},{"op":"predict","col":"x"}]}, open(pp, "w"))
    rows = core.run_pipeline(cp, json.load(open(pp)))
    assert rows[1]["x"] == 1.0
    assert rows[1]["_pred"] == "high"

def test_normalize():
    out = core.normalize([{"a":"0"},{"a":"10"}], ["a"])
    assert out[1]["a"] == 1.0 and out[0]["a"] == 0.0
