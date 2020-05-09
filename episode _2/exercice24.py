#exercice 24
import sys
try:
    r = int(sys.argv[1])
    pi = 3.1415926535897931
    V = 4.0/3.0*pi* r**3
    print('The volume of the sphere is: ',V," pour un ranyon de ",r)
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
