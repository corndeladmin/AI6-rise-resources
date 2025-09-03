from typing import Dict, Any, Tuple
import pandas as pd

def check_null_ratio(series: pd.Series, max_ratio: float) -> str | None:
    """Check if null ratio exceeds threshold."""
    ratio = series.isnull().mean()

    if ratio > max_ratio:
        return f"High null ratio: {ratio:.2f}"
    
    return None

def check_value_range(series: pd.Series, expected_range: Tuple[float, float]) -> str | None:
    """Check if numeric values fall outside expected range."""
    if not pd.api.types.is_numeric_dtype(series):
        return None
    
    min_val, max_val = series.min(), series.max()

    if min_val < expected_range[0] or max_val > expected_range[1]:
        return f"Value out of range: ({min_val}, {max_val})"
    
    return None

def profile_column(series: pd.Series, rules: Dict[str, Any]) -> str | None:
    """Apply profiling checks to a single column."""
    alert = check_null_ratio(series, rules.get("max_null_ratio", 1.0))

    if alert:
        return alert
    if "value_range" in rules:
        return check_value_range(series, rules["value_range"])
    
    return None

def profile_data(df: pd.DataFrame, thresholds: Dict[str, Any]) -> Dict[str, str]:
    """Profile DataFrame and return alerts for rule violations."""
    alerts = {}

    for col in df.columns:
        alert = profile_column(df[col], thresholds.get(col, {}))
        if alert:
            alerts[col] = alert

    return alerts

def main() -> None:
    # Example data ingestion
    df = pd.DataFrame({
        "age": [25, 30, None, 45, 120],
        "income": [50000, 60000, 70000, None, 250000]
    })

    # Example alert configuration
    thresholds = {
        "age": {"max_null_ratio": 0.1, "value_range": (18, 99)},
        "income": {"max_null_ratio": 0.2, "value_range": (10000, 200000)}
    }

    alerts = profile_data(df, thresholds)

    for col, msg in alerts.items():
        print(f"{col}: {msg}")

if __name__ == "__main__":
    main()