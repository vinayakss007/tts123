"""Tests for AI router."""
import pytest

from apps.ai_gateway.router import AIRouter


@pytest.mark.django_db
class TestAIRouter:
    def test_get_provider_openai(self):
        router = AIRouter()
        provider = router.get_provider("openai")
        assert provider.PROVIDER_NAME == "openai"

    def test_get_provider_anthropic(self):
        router = AIRouter()
        provider = router.get_provider("anthropic")
        assert provider.PROVIDER_NAME == "anthropic"

    def test_get_provider_invalid(self):
        router = AIRouter()
        with pytest.raises(ValueError):
            router.get_provider("invalid_provider")
