"""Validation of calculated relationship evidence."""
def validate_result(result):
    missing=[x for x in ("market","company") if not result.get(x)]
    return {"valid":not missing,"missing":tuple(missing),
            "status":result.get("status","unknown")}
