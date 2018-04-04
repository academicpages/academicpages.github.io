---
title: 'visiting Snowdonia'
date: 
comments: true
tags:
  - May holidays
permalink: /posts/2018-05-visiting-Snowdonia/  
comments: true
excerpt: ""
thumbnail: Rembrandt-StoneBridge.jpg
---


Topoi
----------

 + The **northernmos** area: 
   * most popular with tourists 
   * includes places such as  
       + Moel Hebog  
       + Mynydd Mawr and the Nantlle Ridge 
       + Snowdon Massif: Occupies the region between Beddgelert, Pen-y-Pass, and Llanberis.    occupies the area between Beddgelert, Pen-y-Pass and Llanberis It occupies the area between Beddgelert, Pen-y-Pass and Llanberis It occupi  occupies the area between Beddgelert, Pen-y-Pass and Llanberis
       + Glyderau: 
       + Carneddau

 + 

 + Some different paths to Mt. Snowdon (Yr Wyddfa in Welsh).  Mt. Snowdon stands tall over the village of Llanberis 


 Transportation 
------------------------

  "It would be  a real shame to walk up and down the same path in a day." Instead we can explore more distinct terrains, mountains, and villages by using local bus/train.

  +  **Snowdon Sherpa**:  "shuttles around the base of Snowdon connecting all 6 main footpaths and the surrounding villages." 

      * Snowdon Sherpa network map  (PDF) 
      * Network boundary: 
        + SW: Porthmadog 
        + NW: Bangor, and  Caernarfon 
        + SE: Blaenau Ffestiniog (Arriva Trains Wales arrives here from north most city of Llandudno.)
        + East: Betws-y-Coed 
         + NE: Conwy which has interesting Conwy fortress 
                   
      * Timetables for buses S1, S2, S4, S6, S97 (on GWYNEDD COUNCIL website)
      * Ticket prices: single £1.50 and  day ticket: £5.00  
  
  
Weather and ground condition:
----------- 

 + Met Office weather forecast for Snowdon summit. 
 + Snowdonia Ground Conditions: Warnings and information
 
    
  





<script>

function initialize() {
	
  var infoWindow = new google.maps.InfoWindow;
  
  var map = new google.maps.Map(document.getElementById('google-map-1'), { mapTypeId: google.maps.MapTypeId.TERRAIN });
  var bounds = new google.maps.LatLngBounds();
  var points = [ new google.maps.LatLng(53.29, -4.28), new google.maps.LatLng(52.543581, -3.475) ];

  // Extend bounds with each point
  for (var i = 0; i < points.length; i++) { bounds.extend(points[i]); }

  // Apply fitBounds
  map.fitBounds(bounds);
  
  function infoCallback(infowindow, marker) {return function() {
    infowindow.open(map, marker);
    };
  
}

// IMPORT PARK BOUNDARY KML OVERLAY FILE - DO NOT EDIT
var kml1 = new google.maps.KmlLayer("http://www.snowdonia.gov.wales/__data/assets/file/0007/548458/SNPA_parkBoundary.kml",
  { map: map, preserveViewport: true });

var all = [
   /* Hard Strenuous Walk */
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/crimpiau-capel-curig'>Crimpiau, Capel Curig</a><br />Hard Strenuous Walk", "53.10582", "-3.91298"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/llanberis-path'>Llanberis Path, Snowdon</a><br />Hard Strenuous Walk", "53.113187", "-4.12222"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/llanfihangel-path'>Llanfihangel y Pennant Path, Cader Idris</a><br />Hard Strenuous Walk", "52.66120723810418", "-3.965382183598005"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/pyg-track'>PYG Track</a> and <a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/miners-track'>Miners Track</a>, Snowdon<br />Hard Strenuous Walk", "53.08000", "-4.02091"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/minffordd-path'>Minffordd Path, Cader Idris</a><br />Hard Strenuous Walk", "52.68696689981048", "-3.87815190991966"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/pony-path-ty-nant'>Pony Path, T&#375; Nant, Cader Idris</a><br />Hard Strenuous Walk", "52.71939113702029", "-3.929108389963345"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/rhyd-ddu-path'>Rhyd Ddu Path, Snowdon</a><br />Hard Strenuous Walk", "53.0533", "-4.1348"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/snowdon-ranger'>Snowdon Ranger Path, Snowdon</a><br />Hard Strenuous Walk", "53.075272", "-4.139957"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/waen-oer-ridge'>Waen-oer Ridge</a><br />Hard Strenuous Walk", "52.72048142650991", "-3.691419420382994"],
   ["<a href='http://www.snowdonia.gov.wales/visiting/walking/mountain-walks/watkin-path'>Watkin Path, Snowdon</a><br />Hard Strenuous Walk", "53.03505", "-4.04868"]
];
	
  function setMarkers(map, all) {	
    for (var i in all) {	
      var name = all[i][0];
      var lat = all[i][1];
      var lng = all[i][2];
      var latlngset;

      latlngset = new google.maps.LatLng(lat, lng);
      var marker = new google.maps.Marker({ map: map, position: latlngset });
      
      var content1 = '<div class="infowindow-1"><strong>' + name + '</strong></div>';

      var content2 = content1;

      var infowindow = new google.maps.InfoWindow();

      infowindow.setContent(content2);

      google.maps.event.addListener( marker, 'click', infoCallback(infowindow, marker));
      
    }
  }	

// Set all markers in the all variable
setMarkers(map, all); 

};

// Initializes the Google Map
google.maps.event.addDomListener(window, 'resize', initialize);
google.maps.event.addDomListener(window, 'load', initialize);

</script>
