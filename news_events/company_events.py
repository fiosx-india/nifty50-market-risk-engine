"""Company event taxonomy."""
EVENT_TYPES=("earnings","guidance","order","capex","M&A","management","promoter",
             "debt","credit_rating","regulatory","legal","product","capacity","shutdown")
def classify_event(event):
    return event if event.get("type") in EVENT_TYPES else {**event,"type":"other"}
