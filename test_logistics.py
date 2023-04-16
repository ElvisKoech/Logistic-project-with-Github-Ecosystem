from devopslib.logistics import print_cities, calculate_distance, cities
from fastapi.testclient import TestClient
from main import app
import pytest

# def test_distance_btwn_points():
#     city1 = (40.7128, -74.006)  # New York City, New York
#     city2 = (34.0522, -118.2437)  # Los Angeles, California
#     assert calculate_distance(city1, city2) == 3944.422231489921


def test_print_cities(capsys):
    print_cities()
    captured = capsys.readouterr()
    assert "Dallas, Texas" in captured.out


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Logistics INC"}

