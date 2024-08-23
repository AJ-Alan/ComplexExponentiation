# This is a program that computes complex exponentiation
# The standard form will be:
#          (c + di)
# (a + bi)
# where a, b, c, and d are Real numbers
# where the general form of Complex Exponentiation where r = sqrt(a^2 + b^2) and theta = arctan(b/a)
##is: (a + bi)^(c + di) = (r^c)*(e^(-d*theta))*(cos(c*theta + d*ln(r)) + i*sin(c*theta + d*ln(r)))

from math import * #imports math library to use the mathematical functions

def findTheta(a,b):
    # if statements for the base's angle
    if a == 0: # if its purely imaginary, the angle arctangent would be b/0, and python cannot compute that
        if b > 0:
            theta = pi/2 # where arctan(+b/0) = pi/2; and any pure imaginary number either has pi/2 for positive or (-pi/2 or 3pi/2) for negative
        elif b < 0:
            theta = -pi/2 # where arctan(-b/0) = -pi/2
    elif a < 0:# for negative real exponentiation cases
        theta = pi # where arctan(0/a) will not yield a result, but all negative real numbers will have an angle of pi
    else: # otherwise, the normal arctangent will work for these cases
        theta = atan(b/a)
    return theta

def checkComplex(real,imaginary):
    ## if statements for checking if the result is Real, Imaginary, or Complex
    if round(imaginary,4) == 0: #Real results only
        print("\nThe result is Real:\n\t", round(real,4))
    elif round(real,4) == 0: #Imaginary results only
        print("\nThe result is Imaginary:\nRectangular form:\n\t", round(imaginary,4), " * i")
        print("\nPolar form:\n\t[",  round(radius,4), ",",  round(angle,4), "]")
    else: # Complex results only
        print("\nThe result is Complex:\nRectangular form:\n\t", round(real,4), " + ", round(imaginary,4), " * i")
        print("Polar form:\n\t[",  round(radius,4), ",",  round(angle,4), "]")

n = "y"
while (n != "n" and n != "N"):
    n = input("\nDo you want to Calculate exponents?\n>>")
    if n == "y" or n == "Y":
        a = float(input("\ninput a: ")) #input real number a (base)
        b = float(input("\ninput b: ")) #input real number b for imaginary part (base)
        c = float(input("\ninput c: ")) #input real number c (exponent)
        d = float(input("\ninput d: ")) #input real number d for imaginary part (exponent)

        r = sqrt(a*a + b*b) # base's radius
        theta = findTheta(a,b) # base's angle

        angle = c*theta + d*log(r) #new final angle to be inputed to the modified general formula
        radius = (r**c)*exp(-d*theta) #new final radius to be inputed to the modified general formula
        # both of these will be used the Polar Form

        if a == 0 and b == 0 and c == 0: # both forms of 0^0 and 0^i are undefined
            print("\nThe value is undefined")
        else: # otherwise, the general form can be computed
            real = radius*cos(angle) # computes the Real part of the Complex number; the 'a' in "a + bi"
            imaginary = radius*sin(angle) # computes the Imaginary part of the Complex number; the 'b' in "a + bi"
            checkComplex(real,imaginary)

    elif n == "n" or n == "N":
        print("\nBye-bye!")
    else:
        print("\nPlease input y or n only")