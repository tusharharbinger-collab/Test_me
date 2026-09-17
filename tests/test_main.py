from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_healthz():
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_catch_all():
    resp = client.get("/some/path")
    assert resp.status_code == 200
    assert resp.json()["received_path"] == "some/path"
