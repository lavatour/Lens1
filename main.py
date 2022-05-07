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

fp = []
for lightBeam in light:
    """Calculate average focal point"""
    #print(f"fp = {lightBeam.xfp}")
    if lightBeam.xfp != 0:
        fp.append(lightBeam.xfp)
ave = sum(fp) / len(fp)
print(f"ave = {ave}")

#ave_fp = sum(fp) / len(fp)
#print(f"ave = {ave}")

#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_FrontLensSurface(surface)


for lightBeam in light:
    #print(f"beam = {beam}")
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()