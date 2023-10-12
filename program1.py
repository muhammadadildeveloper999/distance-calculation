import googlemaps
import folium

# Replace 'YOUR_API_KEY' with your actual Google Maps API key.
gmaps = googlemaps.Client(key='AIzaSyAEMeWgeUm5zc7D4mjUdh_gkdRdyYf_ZcU')

# Replace these coordinates with your current location.
origin = (37.7749, -122.4194)  # e.g., (37.7749, -122.4194)

# Find multiple hospital locations.
places = gmaps.places_nearby(
    location=origin,
    keyword='hospital',
    rank_by='distance'
)

# Create a folium map centered at your current location.
m = folium.Map(location=origin, zoom_start=15)

for hospital in places['results']:
    name = hospital['name']
    location = hospital['geometry']['location']
    vicinity = hospital['vicinity']
    hospital_location = (location['lat'], location['lng'])

    # Add a marker for each hospital.
    folium.Marker(
        location=hospital_location,
        popup=f"{name}\n{vicinity}"
    ).add_to(m)

# Find the nearest hospital (the first one in the list).
nearest_hospital = places['results'][0]
name = nearest_hospital['name']
location = nearest_hospital['geometry']['location']
vicinity = nearest_hospital['vicinity']
nearest_hospital_location = (location['lat'], location['lng'])

# Add a marker for the nearest hospital with a different icon.
folium.Marker(
    location=nearest_hospital_location,
    popup=f"Nearest Hospital: {name}\n{vicinity}",
    icon=folium.Icon(color='green')
).add_to(m)

# Save the map to an HTML file.
m.save('hospitals_map.html')
