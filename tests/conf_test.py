import pytest
from app.config import settings

@pytest.fixture(autouse=True)
def mock_settings(monkeypatch):
    monkeypatch.setattr(settings, "MANGADEX_USERNAME", "vladivolgin")
    monkeypatch.setattr(settings, "MANGADEX_PASSWORD", "bywpa4-rejbob-Cuxpyc")
    monkeypatch.setattr(settings, "MANGADEX_CLIENT_ID", "personal-client-7a39c96d-46e7-4b79-8f28-a4f18d207298-1b78eb3b")
    monkeypatch.setattr(settings, "MANGADEX_CLIENT_SECRET", "rghnuRq8Nyo3fq6MDyOoW3G9OOZdru3e")