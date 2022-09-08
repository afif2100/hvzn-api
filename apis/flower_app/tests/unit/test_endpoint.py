import falcon
import falcon.testing
import pytest
from helper.health import HealthCheck
from api.hello_name import HelloName

health = HealthCheck()
Name = HelloName()

test_payload = {"name": "hvzn"}
endpoint_prefix = "api/v1"


@pytest.fixture
def client():
    # app route
    app = falcon.App()
    app.add_route("/health", health)
    app.add_route(f"/{endpoint_prefix}/hello", Name)

    return falcon.testing.TestClient(app)


def test_health(client):
    resp = client.simulate_get("/health")

    assert "message" in resp.json
    assert "uptime" in resp.json
    assert resp.json["message"] == "ok"


def test_name(client):
    resp = client.simulate_post(
        "/api/v1/hello",
        json=test_payload,
    )

    assert resp.json["msg"] == "Hello, hvzn!"
