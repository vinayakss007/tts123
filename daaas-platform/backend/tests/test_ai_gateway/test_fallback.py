"""Tests for AI fallback chain."""
import pytest

from apps.ai_gateway.fallback import AllProvidersFailedError, FallbackChain, ProviderHealth


class TestProviderHealth:
    def test_default_healthy(self):
        health = ProviderHealth()
        assert health.is_healthy is True
        assert health.consecutive_failures == 0

    def test_mark_unhealthy(self):
        health = ProviderHealth()
        health.is_healthy = False
        health.consecutive_failures = 3
        assert health.is_healthy is False


class TestFallbackChain:
    def test_init_without_org(self):
        chain = FallbackChain()
        assert chain.organization is None

    def test_all_providers_failed_error(self):
        with pytest.raises(AllProvidersFailedError):
            raise AllProvidersFailedError("All providers failed")
