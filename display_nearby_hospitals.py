import folium
import sqlite3
from geopy.distance import geodesic

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Fetch user's current location (replace with actual user input)
user_latitude = 37.7749
user_longitude = -122.4194

# Create a folium map centered at the user's location
m = folium.Map(location=[user_latitude, user_longitude], zoom_start=15)

# Fetch hospitals from the database
cursor.execute("SELECT FacilityID, FacilityType, Latitude, Longitude FROM Facility")
hospitals = cursor.fetchall()

# Find nearby hospitals and add them to the map
for hospital in hospitals:
    facility_id, facility_type, lat, lon = hospital
    hospital_location = (lat, lon)
    distance = geodesic((user_latitude, user_longitude), hospital_location).miles

    # You can set a distance threshold as per your requirements
    if distance <= 10:  # For example, show hospitals within 10 miles
        folium.Marker(
            location=hospital_location,
            popup=f"{facility_type} (ID: {facility_id})",
        ).add_to(m)

# Save the map to an HTML file
m.save('nearby_hospitals_map.html')

# Close the database connection
conn.close()
 