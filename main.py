"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

from onScreen import Display
from source import Source
from sphericalLens import SphericalLens



#Variables:
"""Source x, y      """

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
lightSourceWidth = 200  #Width or height of light source
numberLightSources = 10
lightSource = Source(numberLightSources, lightSourceWidth)  #Initiate class Source
light = lightSource.createSource()  #Create light object of class Source
print(f"light = {light}")

front = SphericalLens(light)     #Initiate LensFront Class
surface = front.equation()
front.raySurfaceIntersection()

print(f"surface = {surface}")

# theta1
# theta2
#print(front.center)
toScreen = Display()
toScreen.draw_source(light)
toScreen.draw_FrontLensCenter(front.center, 0)
toScreen.draw_FrontLensSurface(surface)

toScreen.display_to_screen()