from devopslib.logistics import (
    print_cities,
    calculate_distance,
    cities,
    travel_time,
    get_city_coordinates,
)
from fastapi.testclient import TestClient
from main import app
import pytest


def test_distance_btwn_points():
    assert (
        calculate_distance("New York City, New York", "Los Angeles, California")
        == 2450.9503446683375
    )


# Build a test for the travel time endpoint
def test_travel_time_endpoint():
    hours = travel_time("New York City, New York", "Los Angeles, California")
    assert hours == 40.84917241113896


def test_travel_time():
    city1 = "New York City, New York"
    city2 = "Los Angeles, California"
    print(get_city_coordinates(city1))  # for debugging
    print(get_city_coordinates(city2))  # for debugging
    expected_time = round(40.84917241113896, 2)
    actual_time = travel_time(city1, city2)
    assert round(actual_time, 2) == expected_time


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


# build a test for the cities endpoint
def test_cities_endpoint(client):
    response = client.get("/cities")
    assert response.status_code == 200
    assert "cities" in response.json()
    assert "Dallas, Texas" in response.json()["cities"]
    assert "San Diego, California" in response.json()["cities"]
    assert "Los Angeles, California" in response.json()["cities"]
    assert "New York City, New York" in response.json()["cities"]


# build a test for the DISTANCE endpoint
def test_distance_endpoint(client):
    response = client.post(
        "/distance",
        json={
            "city1": {"name": "New York City, New York"},
            "city2": {"name": "Los Angeles, California"},
        },
    )
    assert response.status_code == 200
    assert "distance" in response.json()
    assert response.json()["distance"] == 2450.9503446683375
