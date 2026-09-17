"""News normalization interface."""
def normalize_news(item):
    return {"timestamp":item.get("timestamp"),"title":item.get("title",""),
            "source":item.get("source",""),"url":item.get("url",""),
            "symbols":tuple(item.get("symbols",())),"topics":tuple(item.get("topics",()))}
