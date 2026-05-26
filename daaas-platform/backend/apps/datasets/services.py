"""Services for file parsing, storage, and profiling."""
import io
from typing import Any

import pandas as pd

from .models import DataColumn, Dataset


class FileParsingService:
    """Handle file parsing for various formats (CSV, Excel, JSON, Parquet)."""

    SUPPORTED_FORMATS = {"csv", "xlsx", "xls", "json", "parquet", "tsv"}

    def parse_and_profile(self, dataset: Dataset) -> dict[str, Any]:
        """Parse an uploaded file and extract metadata/statistics.

        Returns:
            Dictionary with row_count, column_count, and column metadata.
        """
        df = self._read_file(dataset)

        # Extract column metadata
        columns = []
        for idx, col_name in enumerate(df.columns):
            col_data = df[col_name]
            col_meta = DataColumn(
                dataset=dataset,
                name=col_name,
                data_type=self._infer_type(col_data),
                nullable=col_data.isnull().any(),
                null_count=int(col_data.isnull().sum()),
                unique_count=int(col_data.nunique()),
                position=idx,
                sample_values=col_data.dropna().head(5).tolist(),
            )

            if col_meta.data_type in ("integer", "float"):
                col_meta.min_value = str(col_data.min())
                col_meta.max_value = str(col_data.max())
                col_meta.mean_value = float(col_data.mean())
                col_meta.std_value = float(col_data.std())

            columns.append(col_meta)

        DataColumn.objects.bulk_create(columns)

        return {
            "row_count": len(df),
            "column_count": len(df.columns),
        }

    def _read_file(self, dataset: Dataset) -> pd.DataFrame:
        """Read file from storage into a pandas DataFrame."""
        file_type = dataset.file_type.lower()

        if file_type == "csv":
            return pd.read_csv(dataset.file_path)
        elif file_type == "tsv":
            return pd.read_csv(dataset.file_path, sep="\t")
        elif file_type in ("xlsx", "xls"):
            return pd.read_excel(dataset.file_path)
        elif file_type == "json":
            return pd.read_json(dataset.file_path)
        elif file_type == "parquet":
            return pd.read_parquet(dataset.file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    def _infer_type(self, series: pd.Series) -> str:
        """Infer the DataColumn type from a pandas Series."""
        dtype = series.dtype

        if pd.api.types.is_integer_dtype(dtype):
            return "integer"
        elif pd.api.types.is_float_dtype(dtype):
            return "float"
        elif pd.api.types.is_bool_dtype(dtype):
            return "boolean"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return "datetime"
        elif pd.api.types.is_categorical_dtype(dtype):
            return "categorical"
        else:
            # Check if string column has low cardinality
            if series.nunique() < 20 and len(series) > 100:
                return "categorical"
            return "string"

    def generate_profile(self, dataset: Dataset) -> dict[str, Any]:
        """Generate a comprehensive data profile."""
        df = self._read_file(dataset)
        return {
            "shape": df.shape,
            "memory_usage": int(df.memory_usage(deep=True).sum()),
            "duplicates": int(df.duplicated().sum()),
            "missing_cells": int(df.isnull().sum().sum()),
            "missing_percentage": float(df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100),
        }


class StorageService:
    """Handle file upload/download to S3-compatible storage."""

    def upload_file(self, file, path: str) -> str:
        """Upload a file to object storage and return the path."""
        raise NotImplementedError("Storage service upload not yet implemented")

    def download_file(self, path: str) -> io.BytesIO:
        """Download a file from object storage."""
        raise NotImplementedError("Storage service download not yet implemented")

    def delete_file(self, path: str) -> None:
        """Delete a file from object storage."""
        raise NotImplementedError("Storage service delete not yet implemented")

    def get_presigned_url(self, path: str, expiry: int = 3600) -> str:
        """Generate a pre-signed URL for direct download."""
        raise NotImplementedError("Storage service presigned URL not yet implemented")
