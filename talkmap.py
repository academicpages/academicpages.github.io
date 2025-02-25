# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import getorg
from geopy import Nominatim

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description
    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()
    description = f"{title}<br />{venue}; {location}"

    # Geocode the location and report the status
    location_dict[description] = geocoder.geocode(location)
    print(description, location_dict[description])

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
