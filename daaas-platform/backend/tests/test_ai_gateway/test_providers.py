"""Tests for AI provider implementations."""
import pytest

from apps.ai_gateway.providers import AnthropicProvider, GroqProvider, OllamaProvider, OpenAIProvider
from apps.ai_gateway.providers.base import BaseProvider


class TestBaseProvider:
    def test_openai_provider_is_base_provider(self):
        provider = OpenAIProvider(config={})
        assert isinstance(provider, BaseProvider)

    def test_anthropic_provider_is_base_provider(self):
        provider = AnthropicProvider(config={})
        assert isinstance(provider, BaseProvider)

    def test_groq_provider_is_base_provider(self):
        provider = GroqProvider(config={})
        assert isinstance(provider, BaseProvider)

    def test_ollama_provider_is_base_provider(self):
        provider = OllamaProvider(config={})
        assert isinstance(provider, BaseProvider)


class TestProviderConfig:
    def test_custom_config(self):
        config = {"model": "gpt-4o-mini", "max_tokens": 2048, "temperature": 0.5}
        provider = OpenAIProvider(config=config)
        assert provider.model == "gpt-4o-mini"
        assert provider.max_tokens == 2048
        assert provider.temperature == 0.5
