"""Program to create lens that focuses light on a point near inside the lens and draws the rays."""

import math
from onScreen import Display
from light import Light
from lenses import FirstLens
from lenses import SecondLens
#from linearAlg import LinearAlgebra

"""Initiate Lens object of class Spherical Lens"""
lens1 = FirstLens()     #Initiate Lens Class This will depend on the type of lens being used
surface1 = lens1.equation()      #Equation for the lens surface



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
    lightBeam.refraction1()
    if lightBeam.ray[0][1] == 40:
        print(lightBeam.ray[0][1])
        print(f"lightBeam.angle[-1] = {lightBeam.angle[-1]}")


"""Placement of lens2"""
lens2 = SecondLens()
surface2 = lens2.equation2()

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