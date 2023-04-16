from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn
from devopslib.logistics import (
    calculate_distance,
    print_cities,
    get_city_coordinates,
    travel_time,
)

app = FastAPI()


class City(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home page with GET HTTP method"""
    return {"message": "Hello Logistics INC"}


@app.get("/cities")
async def cities():
    """list of Cities endpoint with GET HTTP method
    Return back a list of cities that are available for further information

    """
    return {"cities": print_cities()}


# build a post method to get distance between two cities
@app.post("/distance")
async def get_distance(city1: City, city2: City):
    """get distance between two cities with POST HTTP method

    Args:
        city1 (City): first city
        city2 (City): second city

    Returns:
        float: distance between cities
    """
    return {
        "distance": calculate_distance(
            get_city_coordinates(city1.name), get_city_coordinates(city2.name)
        )
    }


# build a post method to get travel time  between two cities
@app.post("/travel_time")
async def get_traveltime(city1: City, city2: City):
    """get travel time between two cities with POST HTTP method

    Args:
        city1 (City): first city
        city2 (City): second city

    Returns:
        float: travel time between cities
    """
    hours = travel_time(city1, city2)
    return {"travel_time": f"{hours} hours"}


if __name__ == "__main__":
    uvicorn.run(app)
