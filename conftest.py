import pytest
import os

@pytest.fixture(scope="session", autouse=True)
def api_headers():
    # In Production, you likely need an API Key from GitHub Secrets
    token = os.getenv("PROD_API_TOKEN", "default_mock_token")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
