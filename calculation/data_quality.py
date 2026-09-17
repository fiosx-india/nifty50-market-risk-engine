"""Historical OHLCV quality checks."""
def validate_ohlcv(records):
    if not records:
        return {"valid": False, "errors": ("empty_data",)}
    errors = []
    previous = None
    for i, row in enumerate(records):
        for field in ("timestamp","open","high","low","close","volume"):
            if field not in row or row[field] is None:
                errors.append(f"row_{i}:missing_{field}")
        if any(e.startswith(f"row_{i}:missing_") for e in errors):
            continue
        if float(row["high"]) < max(float(row["open"]), float(row["close"])):
            errors.append(f"row_{i}:invalid_high")
        if float(row["low"]) > min(float(row["open"]), float(row["close"])):
            errors.append(f"row_{i}:invalid_low")
        if previous is not None and str(row["timestamp"]) <= str(previous):
            errors.append(f"row_{i}:non_increasing_timestamp")
        previous = row["timestamp"]
    return {"valid": not errors, "errors": tuple(errors)}

def coverage(records):
    return {
        "count": len(records),
        "start": records[0].get("timestamp") if records else None,
        "end": records[-1].get("timestamp") if records else None,
    }
