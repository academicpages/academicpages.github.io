

import os
from geopy.geocoders import Nominatim
import subprocess

directory = "."
geolocator = Nominatim(user_agent="script")
mapfile="../map/map.html"

map_preamble = """
<!DOCTYPE html>
<html>
<head>

    	<title>Map</title>

    	<meta charset="utf-8" />
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<link rel="shortcut icon" type="image/x-icon" href="docs/images/favicon.ico" />

    	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.0/dist/leaflet.css"/>
    	<script src="https://unpkg.com/leaflet@1.0.0/dist/leaflet.js"></script>

    	<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.css" />
    	<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.Default.css" />
    	<script src="https://unpkg.com/leaflet.markercluster@1.4.1/dist/leaflet.markercluster.js"></script>

</head>

<body>

    	<div id="mapid" style="width: 800px; height: 600px; border: 1px solid #ccc"></div>
    	<script>
            var mymap = L.map('mapid').setView([45,0], 2);

            L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibGVvbmFyZG9wYWNjaWFuaW1vcmkiLCJhIjoiY2ptdnV6Mm05MWJkdTN2bnVsZjA2azBwbCJ9.f6jEjaOydstGXDExvi_ftQ', {maxZoom: 18, attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
                '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                id: 'mapbox.streets'}).addTo(mymap);

            var MarkerIcon = L.Icon.extend({
                options: {shadowUrl: '../map/leaflet_images/marker-shadow.png',
                iconSize:     [25, 41],
                shadowSize:   [41, 41],
                iconAnchor:   [12.5,41],
                shadowAnchor: [13, 41],
                popupAnchor:  [0,-35]
                },
            });

            var blueIcon = new MarkerIcon({iconUrl: '../map/leaflet_images/marker-icon_blue.png'}),
                redIcon = new MarkerIcon({iconUrl: '../map/leaflet_images/marker-icon_red.png'}),
                yellowIcon = new MarkerIcon({iconUrl: '../map/leaflet_images/marker-icon_yellow.png'});

            var clusteredmarkers = new L.MarkerClusterGroup({showCoverageOnHover: false});

            var contributedtalks = L.layerGroup();
            var invitedtalks = L.layerGroup();
            var posters = L.layerGroup();

            var overlays = {
                "Contributed talks": contributedtalks,
                "Invited talks": invitedtalks,
                "Posters": posters
            };

            var baseLayers = {};

"""


map_end = """
</body>
</html>"""

print(map_preamble, file=open(mapfile, "w"))

coord_array = []

counter = 0
for file in os.listdir(directory):
    with open(file, 'r') as f:
        lines = f.read()
        if file.endswith((".md")):
            title_start = lines.find("title: '") + 8 #look for title
            title_trim = lines[title_start:]
            title_end = title_trim.find("'")
            title = title_trim[:title_end]

            date_start = lines.find('date: ') + 6 #look for date
            date_trim = lines[date_start:]
            date_end = date_trim.find('\n')
            date = date_trim[:date_end]

            loc_start = lines.find('location: "') + 11 #look for location
            loc_trim = lines[loc_start:]
            loc_end = loc_trim.find('"')
            location = loc_trim[:loc_end]
            position = geolocator.geocode(location, language='en')
            coord_array.append([position.latitude,position.longitude])
            loc_name = position.address.split(',')[0] +','+ position.address.split(',')[-1]

            type_start = lines.find('type: ') + 6 #look for type
            type_trim = lines[type_start:]
            type_end = type_trim.find('\n')
            type = type_trim[:type_end]
            if "contributed" in type.lower():
                typename = "blueIcon"
            elif "invited" in type.lower():
                typename = "redIcon"
            elif "poster" in type.lower():
                typename = "yellowIcon"

            permalink_start = lines.find('permalink: ') + 11 #look for permalink
            permalink_trim = lines[permalink_start:]
            permalink_end = permalink_trim.find('\n')
            permalink = permalink_trim[:permalink_end]

            marker_data = """            var marker{} = L.marker([{}, {}], {{icon: {}}}).bindPopup('<b>{}</b><br />{}<br /><a href="{}" target="_blank"><i>{}</i></a>');""".format(counter+1,position.latitude,position.longitude,typename,loc_name,date,permalink,title)
            print(marker_data, file=open(mapfile,"a"))
            print('            clusteredmarkers.addLayer(marker{});'.format(counter+1), file=open(mapfile,"a"))
            #if typename is "blueIcon":
            #    print('            contributedtalks.addLayer(marker{});\n'.format(counter+1), file=open(mapfile,"a"))
            #elif typename is "redIcon":
            #    print('            invitedtalks.addLayer(marker{});\n'.format(counter+1), file=open(mapfile,"a"))
            #elif typename is "yellowIcon":
            #    print('            posters.addLayer(marker{});\n'.format(counter+1), file=open(mapfile,"a"))
            counter+=1

markerarray = ''
for num in range(1,counter):
    markerarray += 'marker{}, '.format(num)

markerarray += 'marker{}'.format(counter)




print('\n            mymap.addLayer(clusteredmarkers);', file=open(mapfile, "a"))
print("""            mymap.addLayer(contributedtalks);
            mymap.addLayer(invitedtalks);
            mymap.addLayer(posters);""", file=open(mapfile, "a"))
print('\n\n            var bounds = L.latLngBounds({});'.format(coord_array), file=open(mapfile, "a"))
print("""            mymap.fitBounds(bounds);

            <!--L.control.layers(baseLayers,overlays).addTo(mymap);-->


    	</script>""", file=open(mapfile, "a"))


print(map_end, file=open(mapfile, "a"))
