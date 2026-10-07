"""Central orchestration layer.

Modules contribute evidence; they do not create workflows.
CentralBrain is the single orchestration boundary for MarketContext.
"""

from __future__ import annotations

from typing import Any, Iterable


class ContextOrchestrationModule:
    """Records orchestration metadata without performing market analysis."""

    def analyze(self, context):
        try:
            context.global_evidence["central_brain"] = {
                "status": "completed",
                "orchestration": "CentralBrain",
                "registered_modules": 0,
            }
        except Exception:
            # MarketContext remains usable even if optional diagnostics
            # cannot be stored.
            pass
        return context


class CentralBrain:
    """Single orchestration layer for the research engine."""

    def __init__(self, modules: Iterable[Any] = ()):
        # Always preserve the caller-supplied module contract.
        self.modules = tuple(modules)

        # Metadata is not an analysis workflow. It only records that
        # CentralBrain processed the shared context.
        self._metadata_module = ContextOrchestrationModule()

    def analyze(self, context):
        if context is None:
            raise ValueError("MarketContext cannot be None")

        execution = []

        # First record orchestration state.
        self._metadata_module.analyze(context)

        for module in self.modules:
            name = module.__class__.__name__
            fn = getattr(module, "analyze", None)

            if not callable(fn):
                execution.append({
                    "module": name,
                    "status": "SKIPPED",
                    "reason": "analyze() method not found",
                })
                continue

            try:
                result = fn(context)
                execution.append({
                    "module": name,
                    "status": "COMPLETED",
                    "result_type": type(result).__name__,
                })
            except Exception as exc:
                execution.append({
                    "module": name,
                    "status": "ERROR",
                    "error": str(exc),
                })

                try:
                    context.add_conflict({
                        "type": "module_execution_error",
                        "module": name,
                        "error": str(exc),
                    })
                except Exception:
                    pass

        try:
            context.global_evidence["central_brain"].update({
                "registered_modules": len(self.modules),
                "execution": execution,
                "status": "completed",
            })
        except Exception:
            pass

        return context


__all__ = ["CentralBrain", "ContextOrchestrationModule"]
