"""Model evaluation metrics service."""
from typing import Any


class EvaluationService:
    """Calculate evaluation metrics for trained models."""

    def evaluate(self, model, X_test, y_test, task_type: str) -> dict[str, Any]:
        """Evaluate a trained model and return metrics.

        Args:
            model: Trained scikit-learn model
            X_test: Test features
            y_test: Test targets
            task_type: classification, regression, etc.

        Returns:
            Dictionary of evaluation metrics.
        """
        if task_type == "classification":
            return self._evaluate_classification(model, X_test, y_test)
        elif task_type == "regression":
            return self._evaluate_regression(model, X_test, y_test)
        elif task_type == "clustering":
            return self._evaluate_clustering(model, X_test, y_test)
        else:
            raise ValueError(f"Unknown task type: {task_type}")

    def _evaluate_classification(self, model, X_test, y_test) -> dict[str, Any]:
        """Evaluate classification model with accuracy, precision, recall, F1."""
        from sklearn.metrics import (
            accuracy_score,
            classification_report,
            f1_score,
            precision_score,
            recall_score,
        )

        y_pred = model.predict(X_test)
        return {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred, average="weighted")),
            "recall": float(recall_score(y_test, y_pred, average="weighted")),
            "f1_score": float(f1_score(y_test, y_pred, average="weighted")),
            "classification_report": classification_report(y_test, y_pred, output_dict=True),
        }

    def _evaluate_regression(self, model, X_test, y_test) -> dict[str, Any]:
        """Evaluate regression model with MAE, MSE, RMSE, R2."""
        from sklearn.metrics import (
            mean_absolute_error,
            mean_squared_error,
            r2_score,
        )
        import numpy as np

        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return {
            "mae": float(mean_absolute_error(y_test, y_pred)),
            "mse": float(mse),
            "rmse": float(np.sqrt(mse)),
            "r2_score": float(r2_score(y_test, y_pred)),
        }

    def _evaluate_clustering(self, model, X_test, y_test) -> dict[str, Any]:
        """Evaluate clustering model with silhouette score and inertia."""
        from sklearn.metrics import silhouette_score

        labels = model.predict(X_test) if hasattr(model, "predict") else model.labels_
        return {
            "silhouette_score": float(silhouette_score(X_test, labels)),
            "n_clusters": len(set(labels)),
            "inertia": float(model.inertia_) if hasattr(model, "inertia_") else None,
        }
