import glob
from geopy import Nominatim
import folium
import os

# Set a custom user agent
geocoder = Nominatim(user_agent="personal_website_tiexingwang")

g = glob.glob("_talks/*.md")

location_dict = {}
location = ""

for file in g:
    with open(file, 'r') as f:
        lines = f.read()
        if 'location: "' in lines:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
            
            # Geocode the location and handle possible errors
            try:
                geocoded_location = geocoder.geocode(location)
                if geocoded_location:
                    location_dict[location] = geocoded_location
                    print(f"Geocoded {location}: {geocoded_location}")
                else:
                    print(f"Could not geocode location: {location}")
            except Exception as e:
                print(f"Error geocoding location {location}: {e}")

# Debug: Check the contents of location_dict
print("Location dictionary contents:")
for loc, geo in location_dict.items():
    print(f"{loc}: {geo}")

# Create a map centered around the average coordinates
if location_dict:
    avg_lat = sum([geo.latitude for geo in location_dict.values()]) / len(location_dict)
    avg_lon = sum([geo.longitude for geo in location_dict.values()]) / len(location_dict)
    world_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=2)

    # Add markers to the map
    for loc, geo in location_dict.items():
        folium.Marker([geo.latitude, geo.longitude], popup=loc).add_to(world_map)

    # Save the map to an HTML file
    output_folder = "talkmap"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    map_path = os.path.join(output_folder, "talkmap_tiexingwang.html")
    world_map.save(map_path)
    print(f"Map has been saved as {map_path}")
else:
    print("No locations were successfully geocoded.")
