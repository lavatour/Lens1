"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

import math
from onScreen import Display
from light import Light
from lenses import Lens
#from lenses import SecondLens
#from linearAlg import LinearAlgebra


""" Create Lens1 class object """
lens1 = Lens(300, 500, 0, 1.0, 1.5)
surface1 = lens1.equation()


""" Create lens2 class object """
lens2 = Lens(30, 980, 0, 1.5, 1.0)
surface2 = lens2.equation()


"""Set number of light sources"""
numberLightRays = 20
"""Initiate Class Light"""
light = []  #Light List for light objects

""" Create instances of light"""
for i in range(numberLightRays): #
    light.append(Light(i))

""" LIGHT SOURCE POINTS IN LIGHT OBJECTS """
for lightBeam in light:
    lightBeam.lightSource()


""" LIGHT LENS1 INTERSECTION """
for lightBeam in light:
    lightBeam.rayLensIntersection(lens1)


for lightBeam in light:
    """LIGHT LENS1 REFRACTION."""
    pass
    lightBeam.refraction(lens1, n1 = 1.0, n2 = 1.5)
    print("44")
    #if lightBeam.ray[0][1] == 40:
    #print(f"46 lightBeam.ray[0][1] = {lightBeam.ray[0][1]}")
    #print(f"lightBeam.angle[-1] = {lightBeam.angle[-1]}")


""" LIGHT LENS2 INTERSECTION """
for lightBeam in light:
    lightBeam.rayLensIntersection(lens2)





print("\n****************************************************************\n")
for lightBeam in light:
    """ ray lens2 intersection"""
    pass
    lightBeam.refraction(lens2, n1 = 1.5, n2 = 1.0)
    print()

for lightBeam in light:
    pass
    lightBeam.rayExtension()


#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_Lens1(surface1)
toScreen.draw_Lens2(surface2)

for lightBeam in light:
    #print(f"beam = {beam}")
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()