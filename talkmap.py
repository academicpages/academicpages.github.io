# import pygal
import pygal
  
# import Style class from pygal.style
from pygal.style import Style
  
# create a Style object
custom_style = Style(background='transparent',
			font_family='googlefont:Raleway')
  
# create a world map,
# Style class is used for using
# the custom colours in the map,
worldmap =  pygal.maps.world.World(style = custom_style, show_legend=False)
  
# adding the countries
worldmap.add('talks', {
        'ca' : 3,
        'de' : 1,
        'es' : 1,
        'jp' : 4
})
  
# save into the file
worldmap.render_in_browser()
  
print("Success")
