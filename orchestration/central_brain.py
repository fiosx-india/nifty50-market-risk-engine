"""
Central orchestration layer.

CentralBrain is the sole orchestration layer.
Analysis modules contribute evidence to MarketContext.
Modules do not create independent workflows or trading decisions.
"""

from __future__ import annotations

from typing import Any, Iterable


class CentralBrain:
    """
    Central orchestration engine.

    The brain:
    1. receives the shared MarketContext
    2. executes registered analysis modules
    3. preserves module evidence inside the context
    4. records module failures without destroying the whole pipeline
    5. returns the same MarketContext

    It does not itself calculate indicators, relationships,
    predictions, or trading decisions.
    """

    def __init__(self, modules: Iterable[Any] = ()):
        self.modules = tuple(modules)

    def analyze(self, context):
        """
        Run all registered analysis modules against the shared context.
        """

        if context is None:
            raise ValueError("context cannot be None")

        execution_log = []

        for module in self.modules:
            module_name = module.__class__.__name__

            analyze_fn = getattr(module, "analyze", None)

            if not callable(analyze_fn):
                execution_log.append(
                    {
                        "module": module_name,
                        "status": "skipped",
                        "reason": "analyze() method not found",
                    }
                )
                continue

            try:
                result = analyze_fn(context)

                execution_log.append(
                    {
                        "module": module_name,
                        "status": "completed",
                        "result_type": type(result).__name__,
                    }
                )

            except Exception as exc:
                execution_log.append(
                    {
                        "module": module_name,
                        "status": "error",
                        "error": str(exc),
                    }
                )

                # Keep the pipeline alive and preserve the error
                # as evidence inside MarketContext.
                if hasattr(context, "add_conflict"):
                    context.add_conflict(
                        {
                            "type": "module_execution_error",
                            "module": module_name,
                            "error": str(exc),
                        }
                    )

        # Store orchestration diagnostics without making
        # CentralBrain responsible for analysis calculations.
        if hasattr(context, "global_evidence"):
            context.global_evidence["central_brain"] = {
                "modules_registered": len(self.modules),
                "modules_executed": len(
                    [
                        item
                        for item in execution_log
                        if item["status"] == "completed"
                    ]
                ),
                "execution_log": execution_log,
            }

        return context


__all__ = ["CentralBrain"]
