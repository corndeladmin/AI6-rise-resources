import numpy as np
import pandas as pd
from typing import List, Tuple

# Example 1: Basic List of floats input, float output
def calculate_mean(numbers: List[float]) -> float:
    return 0.0

# Example 2: NumPy array input, NumPy array output
def normalize_array(data_array: np.ndarray) -> np.ndarray:
    return np.array([])

# Example 3: Pandas DataFrame input, Tuple of DataFrame and Series output
def preprocess_dataframe(df: pd.DataFrame, target_column: str) -> Tuple[pd.DataFrame, pd.Series]:
    return pd.DataFrame(), pd.Series(dtype=float)