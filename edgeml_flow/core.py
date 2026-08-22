import csv, json

def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def normalize(rows, cols):
    out = [dict(r) for r in rows]
    for c in cols:
        vals = [float(r[c]) for r in out if r.get(c) not in ("", None)]
        if not vals:
            continue
        lo, hi = min(vals), max(vals)
        span = (hi - lo) or 1.0
        for r in out:
            try:
                r[c] = round((float(r[c]) - lo) / span, 4)
            except Exception:
                pass
    return out

def predict(rows, col):
    vals = [float(r[col]) for r in rows if r.get(col) not in ("", None)]
    if not vals:
        return rows
    mean = sum(vals) / len(vals)
    for r in rows:
        try:
            r["_pred"] = "high" if float(r[col]) >= mean else "low"
        except Exception:
            r["_pred"] = "na"
    return rows

def run_pipeline(csv_path, spec):
    rows = load_csv(csv_path)
    for step in spec.get("steps", []):
        if step["op"] == "normalize":
            rows = normalize(rows, step.get("cols", []))
        elif step["op"] == "predict":
            rows = predict(rows, step["col"])
    return rows
