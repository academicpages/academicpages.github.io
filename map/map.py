import os
from geopy.geocoders import Nominatim
import subprocess

directory_talks = "../_talks"
directory_workshops= "../_wsc"
directory_exp= "../_visits-and-experience"
geolocator = Nominatim(user_agent="script")
mapfile="./map.html"

map_preamble = """
<!DOCTYPE html>
<html>
<head>

    	<title>Map</title>

    	<meta charset="utf-8" />
    	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

    	<link rel="shortcut icon" type="image/x-icon" href="docs/images/favicon.ico" />

    	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"/>
    	<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>

    	<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.css" />
    	<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.Default.css" />
    	<script src="https://unpkg.com/leaflet.markercluster@1.4.1/dist/leaflet.markercluster.js"></script>

        <style>
        body {
            padding: 0;
            margin: 0;
            }
        html, body, #map {
            height: 100%;
            width: 100%;
            }
        </style>


</head>

<body>

    	<div id="mapid" style="width: 100%; height: 100%"></div>
    	<script>
            var mymap = L.map('mapid').setView([45,0], 2);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 20, attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
                '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                'Imagery © <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
                id: 'mapbox.streets'}).addTo(mymap);

            var MarkerIcon = L.Icon.extend({
                options: {shadowUrl: './leaflet_images/marker-shadow.png',
                iconSize:     [25, 41],
                shadowSize:   [41, 41],
                iconAnchor:   [12.5,41],
                shadowAnchor: [13, 41],
                popupAnchor:  [0,-35]
                },
            });

            var blueIcon = new MarkerIcon({iconUrl: './leaflet_images/marker-icon_blue.png'}),
                redIcon = new MarkerIcon({iconUrl: './leaflet_images/marker-icon_red.png'}),
                yellowIcon = new MarkerIcon({iconUrl: './leaflet_images/marker-icon_yellow.png'});
                orangeIcon = new MarkerIcon({iconUrl: './leaflet_images/marker-icon_orange.png'});
                purpleIcon = new MarkerIcon({iconUrl: './leaflet_images/marker-icon_purple.png'});
                tealIcon = new MarkerIcon({iconUrl: './leaflet_images/marker-icon_teal.png'});

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
for file in os.listdir(directory_talks):
    with open(directory_talks+"/"+file, 'r') as f:
        lines = f.read()
        if file.endswith((".md")):
            title_start = lines.find("title: '") + 8 #look for title
            title_trim = lines[title_start:]
            title_end = title_trim.find("'")
            title = title_trim[:title_end]

            type_start = lines.find("type: '") + 7 #look for title
            type_trim = lines[type_start:]
            type_end = type_trim.find("'")
            type = type_trim[:type_end]

            #date_start = lines.find('date: ') + 6 #look for date
            #date_trim = lines[date_start:]
            #date_end = date_trim.find('\n')
            #date = date_trim[:date_end]

            period_start = lines.find('period: "') + 9 #look for period
            period_trim = lines[period_start:]
            period_end = period_trim.find('"')
            period = period_trim[:period_end]

            loc_start = lines.find('location: "') + 11 #look for location
            loc_trim = lines[loc_start:]
            loc_end = loc_trim.find('"')
            location = loc_trim[:loc_end]
            position = geolocator.geocode(location, language='en')
            coord_array.append([position.latitude,position.longitude])
            location = location.split(",")[0]

            venue_start = lines.find('venue: "') + 8 #look for location
            venue_trim = lines[venue_start:]
            venue_end = venue_trim.find('"')
            venue_name = venue_trim[:venue_end]
            #venue_name = position.address.split(',')[0] +','+ position.address.split(',')[-1]

            type_start = lines.find('type: ') + 6 #look for type
            type_trim = lines[type_start:]
            type_end = type_trim.find('\n')
            type = type_trim[:type_end]
            if "contributed" in type.lower():
                typename = "blueIcon"
            elif "invited" in type.lower():
                typename = "redIcon"
            elif "poster" in type.lower():
                typename = "orangeIcon"

            permalink_start = lines.find('permalink: ') + 11 #look for permalink
            permalink_trim = lines[permalink_start:]
            permalink_end = permalink_trim.find('\n')
            permalink = permalink_trim[:permalink_end]

            marker_data = """            var marker{} = L.marker([{}, {}], {{icon: {}}}).bindPopup('<b>{}</b>, {}<br />{}<br />{}<br /><a href="{}" target="_blank"><i>{}</i></a>');""".format(counter+1,position.latitude,position.longitude,typename,venue_name,location,period,type[1:-1],permalink,title)
            print(marker_data, file=open(mapfile,"a"))
            print('            clusteredmarkers.addLayer(marker{});'.format(counter+1), file=open(mapfile,"a"))
            #if typename is "blueIcon":
            #    print('            contributedtalks.addLayer(marker{});\n'.format(counter+1), file=open(mapfile,"a"))
            #elif typename is "redIcon":
            #    print('            invitedtalks.addLayer(marker{});\n'.format(counter+1), file=open(mapfile,"a"))
            #elif typename is "yellowIcon":
            #    print('            posters.addLayer(marker{});\n'.format(counter+1), file=open(mapfile,"a"))
            counter+=1


list_talks = os.listdir(directory_talks)
list_workshops = os.listdir(directory_workshops)
attended_woskshops = list(set(list_workshops)-set(list_talks))
for file in attended_woskshops:
    with open(directory_workshops+"/"+file, 'r') as f:
        lines = f.read()
        title_start = lines.find("title: '") + 8 #look for title
        title_trim = lines[title_start:]
        title_end = title_trim.find("'")
        title = title_trim[:title_end]

        loc_start = lines.find('location: "') + 11 #look for location
        loc_trim = lines[loc_start:]
        loc_end = loc_trim.find('"')
        location = loc_trim[:loc_end]
        position = geolocator.geocode(location, language='en')
        coord_array.append([position.latitude,position.longitude])
        location = location.split(",")[0]

        venue_start = lines.find('venue: "') + 8 #look for venue
        venue_trim = lines[venue_start:]
        venue_end = venue_trim.find('"')
        venue_name = venue_trim[:venue_end]

        link_start = lines.find("link: '") + 7 #look for permalink
        link_trim = lines[link_start:]
        link_end = link_trim.find("'")
        link = link_trim[:link_end]

        period_start = lines.find('period: "') + 9 #look for period
        period_trim = lines[period_start:]
        period_end = period_trim.find('"')
        period = period_trim[:period_end]

        type_start = lines.find('type: ') + 6 #look for type
        type_trim = lines[type_start:]
        type_end = type_trim.find('\n')
        type = type_trim[:type_end]

        if "school" in type.lower():
            typename = "purpleIcon"
        else:
            typename = "tealIcon"

        if lines.find("link: '") == -1:
            marker_data = """            var marker{} = L.marker([{}, {}], {{icon: {}}}).bindPopup('<b>{}</b>, {}<br />{}<br />{}<br /><i>{}</i>');""".format(counter+1,position.latitude,position.longitude,typename,venue_name,location,period,type[1:-1],title)
        else:
            marker_data = """            var marker{} = L.marker([{}, {}], {{icon: {}}}).bindPopup('<b>{}</b>, {}<br />{}<br />{}<br /><a href="{}" target="_blank"><i>{}</i></a>');""".format(counter+1,position.latitude,position.longitude,typename,venue_name,location,period,type[1:-1],link,title)
        print(marker_data, file=open(mapfile,"a"))
        print('            clusteredmarkers.addLayer(marker{});'.format(counter+1), file=open(mapfile,"a"))
        counter+=1


for file in os.listdir(directory_exp):
    with open(directory_exp+"/"+file, 'r') as f:
        lines = f.read()

        loc_start = lines.find('location: "') + 11 #look for location
        loc_trim = lines[loc_start:]
        loc_end = loc_trim.find('"')
        location = loc_trim[:loc_end]
        position = geolocator.geocode(location, language='en')
        coord_array.append([position.latitude,position.longitude])
        #location = location.split(",")[0]

        venue_start = lines.find('venue: "') + 8 #look for venue
        venue_trim = lines[venue_start:]
        venue_end = venue_trim.find('"')
        venue_name = venue_trim[:venue_end]

        period_start = lines.find('period: "') + 9 #look for period
        period_trim = lines[period_start:]
        period_end = period_trim.find('"')
        period = period_trim[:period_end]

        type_start = lines.find('type: ') + 6 #look for type
        type_trim = lines[type_start:]
        type_end = type_trim.find('\n')
        type = type_trim[:type_end]

        typename = "purpleIcon"
        marker_data = """            var marker{} = L.marker([{}, {}], {{icon: {}}}).bindPopup('<b>{}</b>, {}<br />{}<br /><i>{}</i>');""".format(counter+1,position.latitude,position.longitude,typename,venue_name,location,period,type[1:-1])
        print(marker_data, file=open(mapfile,"a"))
        print('            clusteredmarkers.addLayer(marker{});'.format(counter+1), file=open(mapfile,"a"))
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
