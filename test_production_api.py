import pytest
import requests

# Base URL for Production
BASE_URL = "https://jsonplaceholder.typicode.com"

class TestProductionAPI:

    def test_health_check(self):
        """Verify the main endpoint is up"""
        response = requests.get(f"{BASE_URL}/posts/1", timeout=5)
        # We use explicit error messages so they show up in logs
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    def test_api_latency(self):
        """Ensure production response time is under 500ms"""
        response = requests.get(f"{BASE_URL}/posts", timeout=5)
        latency = response.elapsed.total_seconds()
        assert latency < 0.5, f"Performance issue: API took {latency}s"

    def test_data_integrity(self):
        """Verify critical business data structure"""
        response = requests.get(f"{BASE_URL}/users/1", timeout=5)
        data = response.json()

        assert "email" in data, "User record missing email field"
        assert data["email"] == "Sincere@april.biz", f"Unexpected data: {data['email']}"

    @pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/albums"])
    def test_critical_endpoints(self, endpoint):
        """Bulk check critical paths"""
        response = requests.head(f"{BASE_URL}{endpoint}", timeout=5)
        assert response.status_code == 200
