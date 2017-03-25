import math

print("This program finds the real solutions to a quadratic")
try:
    a,b,c = eval(input("Please enter the coefficients(a,b,c)"))
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b + discRoot) / (2 * a)
    print("\nThe solutions are:",root1,root2)
except ValueError as valerr:
    if str(valerr) == "math domain error":
        print("No Real Roots.")
    else:
        print("You didn't give me the right number of coefficients.")
except NameError as namerr:
    print(namerr)
except TypeError as typerr:
    print(typerr)
except SyntaxError as synerr:
    print(synerr)
except:
    print("Something went wrong,sorry")
