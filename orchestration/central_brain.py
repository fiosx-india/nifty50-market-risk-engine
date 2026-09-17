"""Orchestration contract. Modules contribute evidence; they do not create workflows."""
class CentralBrain:
    def __init__(self,modules=()): self.modules=tuple(modules)
    def analyze(self,context):
        for module in self.modules:
            fn=getattr(module,"analyze",None)
            if callable(fn): fn(context)
        return context
