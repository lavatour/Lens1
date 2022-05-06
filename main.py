"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

import math
from onScreen import Display
from light import Light
from sphericalLens import SphericalLens
from linearAlg import LinearAlgebra

"""Lens Surface"""
lensFront = SphericalLens()     #Initiate LensFront Class
surface = lensFront.equation()      #Equation for the lens surface
linAlg = LinearAlgebra
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
    """Calculate ray lens intersection."""
    lensFront.raySurfaceIntersection(lightBeam.ray)
    print(f"ray1 = {lightBeam.ray[-1]}")

for lightBeam in light:
    """Calculate normal angle"""
    unitNormalVector = lensFront.normalVect(lightBeam.ray)
    print(f"normalVector = {unitNormalVector}")

for lightBeam in light:
    """Calculate dot product and multiply normal vector by -1 if necessary"""
    pass
    #dotProd = linAlg.dotProd(self, lightBeam.ray, )

#******************************************8
toScreen = Display()

toScreen.draw_FrontLensSurface(surface)

for source in light:
    #print(f"ray = {source.ray}")
    toScreen.draw_Source(source.ray[0])

for lightBeam in light:
    #print(f"beam = {beam}")
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()