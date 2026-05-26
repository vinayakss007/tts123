"""Data cleaning service for dataset transformation operations."""
from typing import Any

import pandas as pd


class CleaningService:
    """Service for applying data cleaning operations to datasets."""

    def remove_duplicates(self, df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
        """Remove duplicate rows based on specified columns or all columns."""
        if columns:
            return df.drop_duplicates(subset=columns)
        return df.drop_duplicates()

    def fill_missing(self, df: pd.DataFrame, column: str, strategy: str = "mean", value: Any = None) -> pd.DataFrame:
        """Fill missing values in a column using the specified strategy.

        Strategies: mean, median, mode, constant, forward_fill, backward_fill
        """
        if strategy == "mean":
            df[column] = df[column].fillna(df[column].mean())
        elif strategy == "median":
            df[column] = df[column].fillna(df[column].median())
        elif strategy == "mode":
            df[column] = df[column].fillna(df[column].mode()[0])
        elif strategy == "constant":
            df[column] = df[column].fillna(value)
        elif strategy == "forward_fill":
            df[column] = df[column].ffill()
        elif strategy == "backward_fill":
            df[column] = df[column].bfill()
        else:
            raise ValueError(f"Unknown fill strategy: {strategy}")
        return df

    def remove_nulls(self, df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
        """Remove rows containing null values."""
        if columns:
            return df.dropna(subset=columns)
        return df.dropna()

    def normalize(self, df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
        """Normalize columns to 0-1 range (min-max scaling)."""
        for col in columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val != min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
        return df

    def standardize(self, df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
        """Standardize columns to zero mean and unit variance."""
        for col in columns:
            mean = df[col].mean()
            std = df[col].std()
            if std != 0:
                df[col] = (df[col] - mean) / std
        return df

    def remove_outliers(self, df: pd.DataFrame, column: str, method: str = "iqr", threshold: float = 1.5) -> pd.DataFrame:
        """Remove outliers from a column using IQR or z-score method."""
        if method == "iqr":
            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - threshold * iqr
            upper = q3 + threshold * iqr
            return df[(df[column] >= lower) & (df[column] <= upper)]
        elif method == "zscore":
            mean = df[column].mean()
            std = df[column].std()
            z_scores = (df[column] - mean) / std
            return df[z_scores.abs() <= threshold]
        else:
            raise ValueError(f"Unknown outlier method: {method}")
