"""Event-study window preparation."""
def event_window(values,event_index,pre=5,post=20):
    a=max(0,event_index-pre); b=min(len(values),event_index+post+1)
    return {"pre":values[a:event_index],"event":values[event_index:event_index+1],
            "post":values[event_index+1:b]}
