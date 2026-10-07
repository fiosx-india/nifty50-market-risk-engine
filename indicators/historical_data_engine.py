from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable, Sequence

from data_providers.data_normalizer import normalize_records
from data_providers.provider_contract import DataRequest, HistoricalProvider
from schemas.ohlcv import OHLCVRecord


@dataclass(frozen=True)
class HistoricalDataResult:
    """
    Normalized historical OHLCV result.

    This layer is responsible only for obtaining and validating
    historical observations through the provider boundary.
    """

    symbol: str
    timeframe: str
    observations: tuple[OHLCVRecord, ...]
    requested_start: datetime | None
    requested_end: datetime | None
    source: str | None
    status: str
    errors: tuple[str, ...]

    @property
    def sample_size(self) -> int:
        return len(self.observations)

    @property
    def first_timestamp(self) -> datetime | None:
        if not self.observations:
            return None
        return self.observations[0].timestamp

    @property
    def last_timestamp(self) -> datetime | None:
        if not self.observations:
            return None
        return self.observations[-1].timestamp

    def validate(self) -> None:
        if not self.symbol:
            raise ValueError("symbol cannot be empty")

        if not self.timeframe:
            raise ValueError("timeframe cannot be empty")

        if self.status not in {"PASS", "WARN", "FAIL"}:
            raise ValueError(
                "status must be PASS, WARN, or FAIL"
            )

        if self.requested_start is not None:
            _validate_utc_timestamp(self.requested_start)

        if self.requested_end is not None:
            _validate_utc_timestamp(self.requested_end)

        if (
            self.requested_start is not None
            and self.requested_end is not None
            and self.requested_start > self.requested_end
        ):
            raise ValueError(
                "requested_start cannot be later than requested_end"
            )

        previous: datetime | None = None

        for observation in self.observations:
            if not isinstance(observation, OHLCVRecord):
                raise ValueError(
                    "observations must contain OHLCVRecord instances"
                )

            observation.validate()

            if previous is not None:
                if observation.timestamp <= previous:
                    raise ValueError(
                        "observations must be strictly chronological "
                        "with no duplicate timestamps"
                    )

            previous = observation.timestamp


def _validate_utc_timestamp(value: datetime) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    normalized = value.astimezone(timezone.utc)

    return normalized


def _request_value(request: object, name: str):
    return getattr(request, name, None)


def _validate_request(request: DataRequest) -> None:
    if not isinstance(request, DataRequest):
        raise TypeError(
            "request must be a DataRequest"
        )

    symbol = _request_value(request, "symbol")

    if not symbol:
        raise ValueError("request symbol cannot be empty")

    start = _request_value(request, "start")
    end = _request_value(request, "end")

    if start is not None:
        _validate_utc_timestamp(start)

    if end is not None:
        _validate_utc_timestamp(end)

    if start is not None and end is not None:
        if start > end:
            raise ValueError(
                "request start cannot be later than request end"
            )


def _extract_provider_records(result: object) -> Iterable[object]:
    """
    Support provider results exposing records/data/observations
    while keeping this engine independent from vendor-specific APIs.
    """

    if result is None:
        return ()

    for attribute in (
        "records",
        "data",
        "observations",
    ):
        value = getattr(result, attribute, None)

        if value is not None:
            return value

    if isinstance(result, (list, tuple)):
        return result

    raise ValueError(
        "provider result does not expose historical records"
    )


def _extract_provider_source(result: object) -> str | None:
    for attribute in (
        "source",
        "provider",
        "provider_name",
    ):
        value = getattr(result, attribute, None)

        if value:
            return str(value)

    return None


def _extract_provider_errors(result: object) -> tuple[str, ...]:
    errors = getattr(result, "errors", None)

    if errors is None:
        error = getattr(result, "error", None)

        if error:
            return (str(error),)

        return ()

    if isinstance(errors, str):
        return (errors,)

    return tuple(str(item) for item in errors)


def _provider_status(result: object) -> str | None:
    status = getattr(result, "status", None)

    if status is None:
        return None

    return str(status).upper()


class HistoricalDataEngine:
    """
    Orchestrates historical data retrieval and normalization.

    Architecture boundary:

        HistoricalProvider
              ↓
        ProviderResult
              ↓
        DataNormalizer
              ↓
        OHLCVRecord
              ↓
        Calculation modules

    This class does not perform:
      - market prediction
      - correlation
      - relationship scoring
      - BUY/SELL decisions
      - causation claims
    """

    def __init__(
        self,
        provider: HistoricalProvider,
        *,
        source_name: str | None = None,
    ) -> None:
        if provider is None:
            raise ValueError("provider is required")

        self._provider = provider
        self._source_name = source_name

    @property
    def provider(self) -> HistoricalProvider:
        return self._provider

    @property
    def source_name(self) -> str | None:
        return self._source_name

    def fetch(
        self,
        request: DataRequest,
    ) -> HistoricalDataResult:
        """
        Fetch, normalize, and validate historical data.
        """

        _validate_request(request)

        symbol = str(_request_value(request, "symbol"))
        timeframe = str(
            _request_value(request, "timeframe") or ""
        )

        start = _request_value(request, "start")
        end = _request_value(request, "end")

        if start is not None:
            start = _validate_utc_timestamp(start)

        if end is not None:
            end = _validate_utc_timestamp(end)

        try:
            provider_result = self._provider.fetch(request)

        except Exception as exc:
            result = HistoricalDataResult(
                symbol=symbol,
                timeframe=timeframe,
                observations=(),
                requested_start=start,
                requested_end=end,
                source=self._source_name,
                status="FAIL",
                errors=(f"provider error: {exc}",),
            )

            result.validate()
            return result

        provider_errors = _extract_provider_errors(
            provider_result
        )

        provider_status = _provider_status(
            provider_result
        )

        try:
            raw_records = _extract_provider_records(
                provider_result
            )

            normalized = normalize_records(raw_records)

            observations = tuple(normalized)

        except Exception as exc:
            result = HistoricalDataResult(
                symbol=symbol,
                timeframe=timeframe,
                observations=(),
                requested_start=start,
                requested_end=end,
                source=(
                    self._source_name
                    or _extract_provider_source(provider_result)
                ),
                status="FAIL",
                errors=provider_errors
                + (f"normalization error: {exc}",),
            )

            result.validate()
            return result

        source = (
            self._source_name
            or _extract_provider_source(provider_result)
        )

        errors = provider_errors

        if provider_status == "FAIL":
            status = "FAIL"

        elif not observations:
            status = "WARN"
            errors = errors + ("provider returned no observations",)

        elif errors:
            status = "WARN"

        else:
            status = "PASS"

        result = HistoricalDataResult(
            symbol=symbol,
            timeframe=timeframe,
            observations=observations,
            requested_start=start,
            requested_end=end,
            source=source,
            status=status,
            errors=errors,
        )

        result.validate()

        return result

    def fetch_observations(
        self,
        request: DataRequest,
    ) -> tuple[OHLCVRecord, ...]:
        """
        Convenience method returning only normalized observations.
        """

        result = self.fetch(request)

        if result.status == "FAIL":
            message = "; ".join(result.errors)

            raise ValueError(
                f"historical data fetch failed: {message}"
            )

        return result.observations


def load_historical_data(
    provider: HistoricalProvider,
    request: DataRequest,
    *,
    source_name: str | None = None,
) -> HistoricalDataResult:
    """
    Functional convenience wrapper around HistoricalDataEngine.
    """

    engine = HistoricalDataEngine(
        provider,
        source_name=source_name,
    )

    return engine.fetch(request)


def load_historical_observations(
    provider: HistoricalProvider,
    request: DataRequest,
    *,
    source_name: str | None = None,
) -> tuple[OHLCVRecord, ...]:
    """
    Functional convenience wrapper returning normalized observations.
    """

    engine = HistoricalDataEngine(
        provider,
        source_name=source_name,
    )

    return engine.fetch_observations(request)


__all__ = [
    "HistoricalDataResult",
    "HistoricalDataEngine",
    "load_historical_data",
    "load_historical_observations",
]
