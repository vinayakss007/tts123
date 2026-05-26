"""Conftest for AI gateway tests."""
import pytest


@pytest.fixture
def ai_messages():
    """Sample AI messages for testing."""
    return [
        {"role": "system", "content": "You are a data analyst assistant."},
        {"role": "user", "content": "Summarize this dataset."},
    ]
