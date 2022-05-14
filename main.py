"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

import math
from onScreen import Display
from light import Light
from lenses import Lens
#from lenses import SecondLens
#from linearAlg import LinearAlgebra


""" Create Lens1 class object """
lens1 = Lens(300, 500, 0, 1.5)
surface1 = lens1.equation()


""" Create lens2 class object """
lens2 = Lens(30, 965, 0, 1.0)
surface2 = lens2.equation()



"""Set number of light sources"""
numberLightRays = 20
"""Initiate Class Light"""
light = []  #Light List for light objects

""" Create instances of light"""
for i in range(numberLightRays): #
    light.append(Light(i))

"""******** LIGHT SOURCE POINTS IN LIGHT OBJECTS ********"""
for lightBeam in light:
    lightBeam.lightSource()   #Add source coordinates to light.
    #print(f"ray = {lightBeam.ray}")


for lightBeam in light:
    """Calculate ray lens1 intersection."""
    lightBeam.refraction1(lens1)
    #if lightBeam.ray[0][1] == 40:
        #print(lightBeam.ray[0][1])
        #print(f"lightBeam.angle[-1] = {lightBeam.angle[-1]}")



#for lightBeam in light:
    #lightBeam.refraction2()

#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_Lens1(surface1)
toScreen.draw_Lens2(surface2)

for lightBeam in light:
    #print(f"beam = {beam}")
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()