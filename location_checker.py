from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from fuzzywuzzy import fuzz
import time

# List of Moustache properties
properties = [
    {"name": "Moustache Udaipur Luxuria", "lat": 24.57799888, "lon": 73.68263271},
    {"name": "Moustache Udaipur", "lat": 24.58145726, "lon": 73.68223671},
    {"name": "Moustache Udaipur Verandah", "lat": 24.58350565, "lon": 73.68120777},
    {"name": "Moustache Jaipur", "lat": 27.29124839, "lon": 75.89630143},
    {"name": "Moustache Jaisalmer", "lat": 27.20578572, "lon": 70.85906998},
    {"name": "Moustache Jodhpur", "lat": 26.30365556, "lon": 73.03570908},
    {"name": "Moustache Agra", "lat": 27.26156953, "lon": 78.07524716},
    {"name": "Moustache Delhi", "lat": 28.61257139, "lon": 77.28423582},
    {"name": "Moustache Rishikesh Luxuria", "lat": 30.13769036, "lon": 78.32465767},
    {"name": "Moustache Rishikesh Riverside Resort", "lat": 30.10216117, "lon": 78.38458848},
    {"name": "Moustache Hostel Varanasi", "lat": 25.2992622, "lon": 82.99691388},
    {"name": "Moustache Goa Luxuria", "lat": 15.6135195, "lon": 73.75705228},
    {"name": "Moustache Koksar Luxuria", "lat": 32.4357785, "lon": 77.18518717},
    {"name": "Moustache Daman", "lat": 20.41486263, "lon": 72.83282455},
    {"name": "Panarpani Retreat", "lat": 22.52805539, "lon": 78.43116291},
    {"name": "Moustache Pushkar", "lat": 26.48080513, "lon": 74.5613783},
    {"name": "Moustache Khajuraho", "lat": 24.84602104, "lon": 79.93139381},
    {"name": "Moustache Manali", "lat": 32.28818695, "lon": 77.17702523},
    {"name": "Moustache Bhimtal Luxuria", "lat": 29.36552248, "lon": 79.53481747},
    {"name": "Moustache Srinagar", "lat": 34.11547314, "lon": 74.88701741},
    {"name": "Moustache Ranthambore Luxuria", "lat": 26.05471373, "lon": 76.42953726},
    {"name": "Moustache Coimbatore", "lat": 11.02064612, "lon": 76.96293531},
    {"name": "Moustache Shoja", "lat": 31.56341267, "lon": 77.36733331},
]

# Initialize geocoder
geolocator = Nominatim(user_agent="moustache-api")
# Common Indian cities for fuzzy correction
common_cities = [
    "Delhi", "Jaipur", "Udaipur", "Jaisalmer", "Jodhpur", "Agra", "Rishikesh", "Varanasi", "Goa",
    "Koksar", "Daman", "Pushkar", "Khajuraho", "Manali", "Bhimtal", "Srinagar", "Ranthambore",
    "Coimbatore", "Shoja", "Indore", "Bangalore", "Mumbai", "Chennai", "Kolkata", "Hyderabad",
    "Sissu", "Shimla", "Leh", "Ladakh"
]

def correct_spelling(query):
    best_match = max(common_cities, key=lambda city: fuzz.ratio(city.lower(), query.lower()))
    if fuzz.ratio(best_match.lower(), query.lower()) >= 70:
        return best_match
    return query

def get_location_coordinates(place_name):
    location = geolocator.geocode(place_name)
    if location:
        return (location.latitude, location.longitude)
    return None

def find_nearby_properties(query, max_distance_km=50):
    start_time = time.time()
    
    coords = get_location_coordinates(query)
    if not coords:
        return "Could not find location."

    nearby = []

    for prop in properties:
        distance = geodesic(coords, (prop["lat"], prop["lon"])).km
        if distance <= max_distance_km:
            nearby.append((prop["name"], round(distance, 2)))

    end_time = time.time()
    print(f"⏱️ Response Time: {round(end_time - start_time, 2)}s")

    if nearby:
        return f"Nearby Properties:\n" + "\n".join([f"{name} ({dist} km)" for name, dist in sorted(nearby, key=lambda x: x[1])])
    else:
        return "No properties found within 50km."

# === Test ===
if __name__ == "__main__":
    user_input = input("Enter location: ")
    result = find_nearby_properties(user_input)
    print(result)
