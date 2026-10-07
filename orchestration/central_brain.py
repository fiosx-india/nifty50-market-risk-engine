"""
Central orchestration layer for NIFTY 50 Market Risk Engine.

CentralBrain controls execution.
Analysis modules contribute evidence.
CentralBrain itself does not calculate indicators,
relationships, predictions, or trading decisions.
"""

from __future__ import annotations

from typing import Any, Iterable


class CentralBrain:
    """
    Single orchestration layer.

    Modules receive the shared MarketContext and may
    contribute evidence to it.

    A failed optional module must not crash the
    complete application.
    """

    def __init__(self, modules: Iterable[Any] = ()):
        self.modules = tuple(modules)

    def analyze(self, context):
        if context is None:
            raise ValueError("MarketContext cannot be None")

        execution = []

        for module in self.modules:
            name = module.__class__.__name__
            analyze = getattr(module, "analyze", None)

            if not callable(analyze):
                execution.append(
                    {
                        "module": name,
                        "status": "SKIPPED",
                        "reason": "analyze() not available",
                    }
                )
                continue

            try:
                result = analyze(context)

                execution.append(
                    {
                        "module": name,
                        "status": "COMPLETED",
                        "result_type": type(result).__name__,
                    }
                )

            except Exception as exc:
                execution.append(
                    {
                        "module": name,
                        "status": "ERROR",
                        "error": str(exc),
                    }
                )

                # Keep the research pipeline alive.
                try:
                    context.add_conflict(
                        {
                            "type": "module_execution_error",
                            "module": name,
                            "error": str(exc),
                        }
                    )
                except Exception:
                    pass

        # Store orchestration diagnostics only.
        try:
            context.global_evidence["central_brain"] = {
                "registered_modules": len(self.modules),
                "execution": execution,
                "status": "completed",
            }
        except Exception:
            pass

        return context


__all__ = ["CentralBrain"]
