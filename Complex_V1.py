## Complex Expontentiation
## set (a + bi)^(c + di), where r = sqrt(b^2 + a^2), theta = Arctan(b/a) + 2*pi*n, thetaVnull = Arctan(b/a) (principal value)
## as (a + bi)^(c + di) = r^c * e^(-d*theta) * (cos(c*theta + d*log(r)) + i*sin(c*theta + d*log(r)))
## where it will be represented as two values: real = r^c * e^(-d*theta) * cos(c*theta + d*log(r)) and imaginary = r^c * e^(-d*theta) * sin(c*theta + d*log(r))
import math
print ("\n\nWelcome to the Complex Expontentiation calculator!\nThe form is (a + bi)^(c + di)")

## would you like to use the calculator? 

a = float(input("\nPlease enter a value for a: "))
b = float(input("\nPlease enter a value for b: "))
c = float(input("\nPlease enter a value for c: "))
d = float(input("\nPlease enter a value for d: "))

## radius
r = math.sqrt(a*a + b*b)

## original theta -> before exponentiation
if a == 0:
    if b > 0:
        theta = math.pi/2
    elif b < 0:
        theta = -math.pi/2
elif a < 0:
    theta = math.pi
else:
    theta = math.atan(b/a)

## input theta after exponentiation
angle = c*theta+d*math.log(r)
## new radius after exponentiation
radius = (r**c)*math.exp(-d*theta)

if a == 0 and b == 0 and c == 0:
    print("result is undefined")
else:
    real = radius*math.cos(angle)
    imaginary = radius*math.sin(angle)
    if round(real,4) == 0: ## purely imaginary
        print("\n\nThe result is Purely Imaginary:")
        print("Rectangular form:\n\t", round(real,4), " + ", round(imaginary,4), "* i")
        print("Polar form:\n\t[",round(radius,4),",",round(angle,4),"]")
        print("\n\n")
    elif round(imaginary,4) == 0: ## purely real
        print("\n\nThe result is Purely Real: ", round(real,4))
        print("\n\n")
    else: ## exclusively complex
        print("\n\nThe result is Complex:")
        print("Rectangular form:\n\t", round(real,4), " + ", round(imaginary,4), "* i")
        print("Polar form:\n\t[",round(radius,4),",",round(angle,4),"]")
        print("\n\n")
 

# if b == 0 and d == 0: ## purely Reals -> (a + 0) ^ (c + 0)
#     # from
#     if a < 0:
#         if c == 1/2:
#             result = pow(abs(a),c)
#             print("\n\nThe result is", result,"* i (Purely Imaginary).\n\n")
#         elif c < 1/2 and (0.5)%c == 0:
#             print("\n\nCurrently, the result is Exclusively Complex (not computable yet).\n\n")
#         else:
#             result = pow(a,c)
#             print("\n\nThe result is", result, "\n\n")
#     elif a == 0 and c == 0:
#         print("\n\n0^0 is Undefined.\n\n")
#     else:
#         result = pow(a,c)
#         print("\n\nThe result is", result, "(Real).\n\n")
#     # can be reused for the Imaginary by Reals
# elif a == 0 and c == 0: ## purely Imaginary -> (0 + bi) ^ (0 + di)
#     if b == 0:
#         print("\n\n0^i is Undefined.\n\n")
#     elif b == 1 or b == -1:
#         print("\n\nresult is Real\n\n")
#     elif d == (math.pi/(2*(math.log(abs(b))))) or d == (-math.pi/(2*(math.log(abs(b))))): ## d must be +/- pi/2 + 2*pi*n <- function checker
#         print("\n\nresult is Purely Imaginary.\n\n")
#     else:
#         print ("\n\nresult is Exclusively Complex\n\n")
# elif b == 0 and c == 0: ## Reals by Imaginary -> (a + 0) ^ (0 + di)
#     if a == 0:
#         print("\n\n0^i is Undefined.\n\n")
#     elif a == 1 or a == -1:
#         print("\n\nresult is Real\n\n")
#     elif d == (math.pi/(2*(math.log(abs(a))))) or d == (-math.pi/(2*(math.log(abs(a))))): ## d must be +/- pi/2 + 2*pi*n <- function checker
#         print("\n\nresult is Purely Imaginary.\n\n")
#     else:
#         print ("\n\nresult is Exclusively Complex\n\n")
# ## note: a^di and (bi)^di have the same base code... how do I resolve this

# elif a == 0 and d == 0:
#     if b > 0:
#         theta = math.pi/2
#     elif b < 0:
#         theta = -math.pi/2
#     if b == 0 and c == 0:
#         print("\n\n0^0 is Undefined.\n\n")
#     else:
#         real = math.pow(abs(b),c) * math.cos(c*theta)
#         imaginary = math.pow(abs(b),c) * math.sin(c*theta)
#         print("\n\nThe result is ", real, " + ", imaginary, "* i\n\n")

    