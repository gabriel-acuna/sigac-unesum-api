import pytest
import requests
from httpx import AsyncClient
from app.api.routes import app
from decouple import config
from fastapi.testclient import TestClient


client = TestClient(app)
token = None
response = client.post('/api/login',  json={
    'email': config('ADMIN_EMAIL'),
    'password': config('ADMIN_PASS')})
if response.status_code == 200:
    r = response.json()
    token = r['token']


@pytest.fixture(scope="function")
async def test_app():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac,  {"Authorization": f"Bearer {token}"}
