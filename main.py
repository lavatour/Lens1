"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

import math
from onScreen import Display
from light import Light
from sphericalLens import SphericalLens
#from linearAlg import LinearAlgebra

"""Initiate Lens object of class Spherical Lens"""
lens = SphericalLens()     #Initiate Lens Class This will depend on the type of lens being used
surface = lens.equation()      #Equation for the lens surface

"""Set number of light sources then initiate ray objects"""
numberLightSources = 20
"""Initiate Class Light"""

light = []  #Light List for light objects
for i in range(numberLightSources): #
    light.append(Light(i))   #Initiation of light objects

for lightBeam in light:
    lightBeam.source()   #Add source coordinates to light.
    #print(f"ray = {lightBeam.ray}")


for lightBeam in light:
    """Calculate ray lens intersection."""
    lightBeam.refraction()



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