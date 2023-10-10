# import requests
# import folium
# from geopy.geocoders import Nominatim
# import polyline

# # Replace 'YOUR_API_KEY' with your Google Maps API Key
# API_KEY = 'AIzaSyAEMeWgeUm5zc7D4mjUdh_gkdRdyYf_ZcU'

# # Initialize the geocoder
# geocoder = Nominatim(user_agent="i know python!")

# # Input locations from the user
# location1 = input("Enter the starting location: ")
# location2 = input("Enter the destination location: ")

# coordinates1 = geocoder.geocode(location1)
# coordinates2 = geocoder.geocode(location2)

# if coordinates1 is None:
#     print(f"Starting location '{location1}' not found.")
# elif coordinates2 is None:
#     print(f"Destination location '{location2}' not found.")
# else:
#     origin = f"{coordinates1.latitude},{coordinates1.longitude}"
#     destination = f"{coordinates2.latitude},{coordinates2.longitude}"

#     # Make a request to the Google Maps Directions API
#     url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}"
#     response = requests.get(url)
#     data = response.json()

#     if data.get("status") == "OK" and "routes" in data and data["routes"]:
#         # Extract and print turn-by-turn directions
#         directions = []
#         for step in data["routes"][0]["legs"][0]["steps"]:
#             directions.append(step["html_instructions"])

#         # Join the directions into a single string and print it
#         directions_text = "\n".join(directions)
#         print("\nTurn-by-turn directions:")
#         print(directions_text)

#         # Extract the route as a polyline
#         route = data["routes"][0]["overview_polyline"]["points"]
#         decoded_route = polyline.decode(route)

#         # Create a map centered on the starting location
#         m = folium.Map(location=[coordinates1.latitude, coordinates1.longitude], zoom_start=10)

#         # Add markers for the starting and destination locations
#         folium.Marker([coordinates1.latitude, coordinates1.longitude], tooltip=location1).add_to(m)
#         folium.Marker([coordinates2.latitude, coordinates2.longitude], tooltip=location2).add_to(m)

#         # Add the decoded route to the map
#         folium.PolyLine(locations=decoded_route, color="blue", weight=5, opacity=0.7).add_to(m)

#         # Save the map as an HTML file or display it in Jupyter Notebook
#         m.save("route_map.html")
#     else:
#         print("Directions not found. Please check the locations or try a different pair of locations.")


