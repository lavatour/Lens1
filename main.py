"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

from onScreen import Display
from source import Source


#Variables:


"""
Lens Variables
# deltaY
# deltaY: a fixed vertical value between points
# deltaX: The amount that x changes. Determined by the slope of the lens
# lensSlope
"""

"""
Light Variables
source
sourceNum
sourceWidth
sourceX, sourceY
"""
lightSourceWidth = 200
numberLightSources = 10
lightSource = Source(numberLightSources, lightSourceWidth)
light = lightSource.createSource()

# theta1
# theta2
#


toScreen = Display()
toScreen.draw_source(light)

toScreen.display_to_screen()