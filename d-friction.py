#Author: Robert Markoski
#URL: http://www.RobertMarkoski.net/Engineering
#Description: Iterative Calculation of D'Arcy-Weisbach Friction Factor via the Colebrook-White Equation.
"""
The D'Arcy Friction Factor is used extensivley in fluid system design.
Calculating its value can often be cumbersome, and prone to error when performed by hand.
The following little program/function will calculate the D'Arcy Friction Factor given values for the Reynolds Number, Pipe Diameter and Pipe Roughness

Now obviously you can use the several approximations of the implicit Colebrook-White equation such as the Swammee-Jain Equation (which I have also included a function for, it takes the same inputs as the Colebrook-White Equation.
As for most applications 4 significant figures is all that is required, either equation may be used.

Colebrook Equation - http://en.wikipedia.org/wiki/.........
D'Arcy Friction Factor - http.////
Swamee Jain Equation


You are obviously free to use this in any way/shape/form with or without my attribution.
I am only human however and am not liable if anything goes wrong whilst you use this program. If you are a good engineer you would check and triple check all your values.
"""
import math # Import Handy Math Functions

######## EDIT THESE VALUES #######
flow = 25           # Flow in L/s
diameter = 0.14636  # Pipe Diameter in m
roughness = 0.007   # Pipe Roughness in mm
density = 1020      # Density of Fluid in kg/m3
viscosity = 0.001   # Visocsity of Fluid in Pa s
##################################

pipearea = diameter**2 / 4 * math.pi #Pipe Area in m^2

velocity = (flow/1000)/pipearea #Flow Velocity in m/s

reynolds = velocity*diameter*density/viscosity # Reynolds Number for Full Circula Pipe

def CalculateF(diameter,roughness,reynolds):
    friction = 0.08 #Starting Friction Factor
    while 1:
        leftF = 1 / friction**0.5 #Solve Left side of Eqn
        rightF = - 2 * math.log10(2.51/(reynolds * friction**0.5)+(roughness/1000)/(3.72*diameter)) # Solve Right side of Eqn
        friction = friction - 0.000001 #Change Friction Factor
        if (rightF - leftF <= 0): #Check if Left = Right
            break
    return friction

def SwameeJain(diameter, roughness, reynolds):
    return 0.25 / (math.log10((roughness/1000)/(3.7*diameter)+5.74/(reynolds**0.9)))**2

friction = CalculateF(diameter,roughness,reynolds)
print("Reynolds Number is {:.0f}".format(reynolds))
print("Darcy Friction Factor is {:.4f}".format(friction))
print("Swamee-Jain - Darcy Friction Factor is {:.4f}".format(SwameeJain(diameter,roughness,reynolds)))
