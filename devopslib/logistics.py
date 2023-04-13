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
import geopy
from geopy.distance import geodesic
#build a list of 10 cities in the usa and their coordinates

cities = [
    {"city": "New York City, New York", "lat": 40.7128, "lng": -74.0060},
    {"city": "Los Angeles, California", "lat": 34.0522, "lng": -118.2437},
    {"city": "Chicago, Illinois", "lat": 41.8781, "lng": -87.6298},
    {"city": "Houston, Texas", "lat": 29.7604, "lng": -95.3698},
    {"city": "Phoenix, Arizona", "lat": 33.4484, "lng": -112.0740},
    {"city": "Philadelphia, Pennsylvania", "lat": 39.9526, "lng": -75.1652},
    {"city": "San Antonio, Texas", "lat": 29.4241, "lng": -98.4936},
    {"city": "San Diego, California", "lat": 32.7157, "lng": -117.1611},
    {"city": "Dallas, Texas", "lat": 32.7767, "lng": -96.7970},
    {"city": "San Jose, California", "lat": 37.3382, "lng": -121.8863}
]

def calculate_distance(city1, city2):
    city1_lat, city1_lng = None, None
    city2_lat, city2_lng = None, None
    for city in cities:
        if city["city"] == city1:
            city1_lat, city1_lng = city["lat"], city["lng"]
        elif city["city"] == city2:
            city2_lat, city2_lng = city["lat"], city["lng"]
        if city1_lat is not None and city2_lat is not None:
            break
    distance = geodesic((city1_lat, city1_lng), (city2_lat, city2_lng)).km
    return distance

# Example usage
distance = calculate_distance("New York City, New York", "Los Angeles, California")
print(f"{distance} km") # Output: 3947.026423034262
