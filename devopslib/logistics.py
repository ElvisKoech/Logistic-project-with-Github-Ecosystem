"""
This module deals with logistics and calculates distances between two points
and the time it takes to travel between two points and other logistics related questions
for a given speed
Example this function calculate the distance between two cities:
from geopy import distance
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).miles)
538.39044536

"""
# from geopy.distance import distance
from geopy.distance import geodesic

cities = {
    "New York City, New York": (40.7128, -74.0060),
    "Los Angeles, California": (34.0522, -118.2437),
    "Chicago, Illinois": (41.8781, -87.6298),
    "Houston, Texas": (29.7604, -95.3698),
    "Phoenix, Arizona": (33.4484, -112.0740),
    "Philadelphia, Pennsylvania": (39.9526, -75.1652),
    "San Antonio, Texas": (29.4241, -98.4936),
    "San Diego, California": (32.7157, -117.1611),
    "Dallas, Texas": (32.7767, -96.7970),
    "San Jose, California": (37.3382, -121.8863),
}


def calculate_distance(city1, city2):
    """Calculates the distance between two cities using geopy.distance"""
    return geodesic(cities[city1], cities[city2]).miles


# # return the coordinates of the city
def get_city_coordinates(city):
    """Returns the coordinates of a city"""

    for city_name, coordinates in cities.items():
        if city_name == city:
            return city_name
        elif city_name == city:
            return coordinates


def print_cities():
    city_names = []
    for city in cities:
        city_names.append(city)
        print(city)
    return city_names


# estimate the travel time between two cities by car
def travel_time(city1, city2, speed=60):
    """Estimates the travel time between two cities by car
    given a default speed of 60 mph
    """
    return (
        calculate_distance(get_city_coordinates(city1), get_city_coordinates(city2))
        / speed
    )


# print_cities()

# distance_btwn_cities = calculate_distance(
#     "New York City, New York", "Los Angeles, California"
# )
# print(f"{distance_btwn_cities} miles")  # Output: 2450.9503446683375
# time_btwn_cities = travel_time(
#     "New York City, New York", "Los Angeles, California"
# )
# print(f"{time_btwn_cities} hours")  # Output: 2450.9503446683375
