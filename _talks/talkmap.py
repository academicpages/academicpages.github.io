

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy import Nominatim


g = glob.glob("*.md")


geocoder = Nominatim(user_agent="your_app_name")
location_dict = {}
location = ""
permalink = ""
title = ""

import time

for file in g:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]

        try:
            location_dict[location] = geocoder.geocode(location)
            print(location, "\n", location_dict[location])
        except Exception as e:
            print(f"Error geocoding {location}: {e}")
            location_dict[location] = None

        if location:
            try:
                location_dict[location] = geocoder.geocode(location)
                print(location, "\n", location_dict[location])
            except Exception as e:
                print(f"Error geocoding {location}: {e}")
                location_dict[location] = None
            time.sleep(1)
        else:
            print("No location found in file.")

valid_location_dict = {k: v for k, v in location_dict.items() if v is not None}

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(valid_location_dict, folder_name="../talkmap", hashed_usernames=False)





