#Author: Robert Markoski
#URL: http://www.RobertMarkoski.net
#Description: Iterative Calculation of D'Arcy-Weisbach Friction Factor via the Colebrook-White Equation.
"""
The D'Arcy Friction Factor is used extensivley in fluid system design.
Calculating its value can often be cumbersome, and prone to error when performed by hand.
The following little program/function will calculate the D'Arcy Friction Factor given values for the Reynolds Number, Pipe Diameter and Pipe Roughness

Colebrook Equation - http://en.wikipedia.org/wiki/Darcy_friction_factor_formulae#Colebrook_equation
Swamee Jain Equation -http://en.wikipedia.org/wiki/Darcy_friction_factor_formulae#Swamee.E2.80.93Jain_equation

You are free to use this in any way/shape/form with or without my attribution.
I am not liable if anything goes wrong whilst you use this program.
"""
import math # Import Handy Math Functions

flow = raw_input("Please enter Flowrate in L/s: ")
diameter = raw_input("Please enter Pipe Internal Diameter in mm: ")
roughness = raw_input("please enter Material Roughness in mm [0.007]: ")
density = raw_input("Please enter Fluid Density in kg/m3 [998]: ")
viscosity = raw_input("Please enter Fluid Viscosity in Pa.s [0.001]: ")

if not roughness:
    roughness = 0.007 #Default HDPE
if not density:
    density = 998    #Default Ddensity of water @ 20C
if not viscosity:
    viscosity = 0.001 #Default Viscosty of Water @ 20C

#Turn all values into floating points
flow = float(flow)
diameter = float(diameter)/1000
roughness = float(roughness)
density = float(density)
viscosity = float(viscosity)


pipearea = diameter**2 / 4 * math.pi #Pipe Area in m^2

velocity = (flow/1000)/pipearea #Flow Velocity in m/s

reynolds = velocity*diameter*density/viscosity # Reynolds Number for Full Circula Pipe

def CalculateF(diameter,roughness,reynolds):
    friction = 0.08 #Starting Friction Factor
    while 1:
        leftF = 1 / friction**0.5 #Solve Left side of Eqn
        rightF = - 2 * math.log10(2.51/(reynolds * friction**0.5)+(roughness/1000)/(3.72*diameter)) # Solve Right side of Eqn
        friction = friction - 0.000001 #Change Friction Factor
      #  print(leftF)
      #  print(rightF)
      #  print(friction)
        if (rightF - leftF <= 0): #Check if Left = Right
            break
    return friction

def SwameeJain(diameter, roughness, reynolds):
    return 0.25 / (math.log10((roughness/1000)/(3.7*diameter)+5.74/(reynolds**0.9)))**2

friction = CalculateF(diameter,roughness,reynolds)

#Print results in nice 'table'
print("\n------------RESULTS-------------")
print("Reynolds Number\t|\t{:.0f}".format(reynolds))
print("Velocity (m/s)\t|\t{:.3f}".format(velocity))
print("---------FRICTION FACTOR--------")
print("Colebrook-White\t|\t{:.4f}".format(friction))
print("Swamee-Jain\t|\t{:.4f}".format(SwameeJain(diameter,roughness,reynolds)))
