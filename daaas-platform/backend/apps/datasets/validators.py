"""Validators for dataset uploads and data quality."""
from django.conf import settings
from rest_framework.exceptions import ValidationError


class FileTypeValidator:
    """Validate uploaded file type against allowed extensions."""

    ALLOWED_EXTENSIONS = {"csv", "xlsx", "xls", "json", "parquet", "tsv"}

    def validate(self, file) -> None:
        extension = file.name.rsplit(".", 1)[-1].lower() if "." in file.name else ""
        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValidationError(
                f"Unsupported file type: .{extension}. "
                f"Allowed types: {', '.join(sorted(self.ALLOWED_EXTENSIONS))}"
            )


class FileSizeValidator:
    """Validate uploaded file size against configured limit."""

    def validate(self, file) -> None:
        max_size = getattr(settings, "MAX_UPLOAD_SIZE_MB", 500) * 1024 * 1024
        if file.size > max_size:
            raise ValidationError(
                f"File size ({file.size / 1024 / 1024:.1f} MB) exceeds "
                f"maximum allowed size ({settings.MAX_UPLOAD_SIZE_MB} MB)."
            )


class DatasetValidator:
    """Run data quality validations on a dataset."""

    def validate(self, dataset) -> dict:
        """Validate data quality and return report."""
        issues = []

        if dataset.row_count == 0:
            issues.append({"severity": "error", "message": "Dataset has no rows"})

        if dataset.column_count == 0:
            issues.append({"severity": "error", "message": "Dataset has no columns"})

        # Check for high null ratio columns
        for column in dataset.columns.all():
            if dataset.row_count and column.null_count > 0:
                null_ratio = column.null_count / dataset.row_count
                if null_ratio > 0.5:
                    issues.append({
                        "severity": "warning",
                        "column": column.name,
                        "message": f"Column has {null_ratio:.0%} null values",
                    })

        return {
            "is_valid": not any(i["severity"] == "error" for i in issues),
            "issues": issues,
            "issue_count": len(issues),
        }
