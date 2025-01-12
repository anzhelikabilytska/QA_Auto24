import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logging.basicConfig(
    filename="test_search.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@pytest.fixture(scope="class")
def auth_session():
    base_url = "http://127.0.0.1:8080"
    session = requests.Session()

    auth_response = session.post(
        f"{base_url}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )
    assert auth_response.status_code == 200, "Authentication failed"

    access_token = auth_response.json().get("access_token")
    assert access_token, "No access token returned"

    session.headers.update({"Authorization": f"Bearer {access_token}"})
    return session


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 10),
        ("engine_volume", 3),
        (None, 7),
        ("brand", None),
        ("price", None),
        (None, None),
    ]
)
def test_search_cars(auth_session, sort_by, limit):
    base_url = "http://127.0.0.1:8080"
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    response = auth_session.get(f"{base_url}/cars", params=params)

    logging.info("GET /cars params=%s", params)
    logging.info("Response: %s", response.json())

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert isinstance(response.json(), list), "Response is not a list"

    if limit:
        assert len(response.json()) <= limit, "Number of results exceeds the limit"
