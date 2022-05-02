"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

from onScreen import Display
from light import Light
from sphericalLens import SphericalLens

"""Lens Surface"""
lensFront = SphericalLens()     #Initiate LensFront Class
surface = lensFront.equation()      #Equation for the lens surface
#print(f"surface = {surface}")   #Print surface coordinates

"""Light Source"""
#lightSourceWidth = 600  #Width or height of light source
numberLightSources = 20

light = []  #Light List for light objects
for i in range(numberLightSources): #
    light.append(Light(i))          #Initiation of light objects

for lightBeam in light:
    lightBeam.source()   #Add source coordinates to light.
    #print(f"ray = {lightBeam.ray}")

for lightBeam in light:
    pass
    #print(f"lightBeam.ray = {lightBeam.ray}")

for lightBeam in light:
    lensFront.raySurfaceIntersection(lightBeam.ray)
    print(f"ray1 = {lightBeam.ray}")

toScreen = Display()

toScreen.draw_FrontLensSurface(surface)

for source in light:
    #print(f"ray = {source.ray}")
    toScreen.draw_Source(source.ray[0])

for lightBeam in light:
    #print(f"beam = {beam}")
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()