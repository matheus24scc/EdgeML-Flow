import argparse, json
from edgeml_flow import core

def main(argv=None):
    p = argparse.ArgumentParser(prog="EdgeML-Flow", description="Roda pipeline ML leve sobre CSV.")
    p.add_argument("csv")
    p.add_argument("pipeline", help='JSON {"steps":[{"op":"normalize","cols":["x"]},{"op":"predict","col":"x"}]}')
    args = p.parse_args(argv)
    spec = json.load(open(args.pipeline))
    rows = core.run_pipeline(args.csv, spec)
    hi = sum(1 for r in rows if r.get("_pred") == "high")
    print("linhas=%d high=%d" % (len(rows), hi))
    return 0
