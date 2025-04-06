# Reflection: Moustache Property Locator Assignment

## 1. What was your initial thought process when you first read the problem statement, and how did you break it down into smaller, manageable parts?

When I read the problem statement, my first thought was to clearly separate the challenge into three key components:
- Convert the user’s location query to geographic coordinates.
- Compare that location against a fixed list of Moustache properties.
- Return all properties within a 50 km radius of the location, sorted by distance.

To do this, I broke it down into these steps:
1. Handle user input and fix minor spelling errors.
2. Convert city/place name to latitude and longitude using geolocation.
3. Measure distance to each property using geodesic distance.
4. Optimize and respond quickly, with a fast API response.

## 2. What specific tools, libraries, or online resources did you use to develop your solution, and why did you choose them over other options?

- **FastAPI** – It’s lightweight, fast, and great for building APIs quickly. I also like its clean routing and automatic docs.
- **Geopy** – To convert city names to coordinates and calculate distances between locations.
- **fuzzywuzzy** – For simple and effective fuzzy string matching to handle typos in city names.
- **Uvicorn** – As the ASGI server to run the FastAPI app.
- **Python 3.11** – My dev language and version.
- **Git & GitHub** – For version control and submission.

I preferred these over more complex frameworks (like Django) to keep the API minimal, fast, and readable.

## 3. Describe a key challenge you faced while solving this problem and how you arrived at the final solution?

One key challenge was **handling typos in user input**. If a user typed "Udaipurr" or "Rishiksh", I didn’t want the API to fail silently. Using `fuzzywuzzy` with a curated list of cities helped me match misspelled queries to real destinations with decent accuracy.

Another challenge was the **geolocation accuracy and speed**. Since I used the Nominatim geocoder (from `geopy`), I had to ensure that the input string was clean and matched real locations. I made sure the app responded gracefully when the location wasn’t found, returning a helpful error message instead of crashing.

## 4. If you had more time, what improvements or alternative approaches would you explore, and why do you think they might be valuable?

- **Use RapidFuzz instead of fuzzywuzzy** – It’s faster and more actively maintained.
- **Implement caching for geolocation results** – To avoid repeated API calls for the same locations.
- **Add a frontend or minimal UI** – To visualize nearby properties on a map.
- **Integrate a faster geocoding service** – Like Google Places API or Mapbox for more accurate and reliable results.
- **Containerize with Docker** – For easy deployment and testing.

Overall, I would focus on performance improvements, caching, and enhancing the user experience.
