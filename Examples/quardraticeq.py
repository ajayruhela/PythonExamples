'''ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0'''

import cmath
import re

gonext = 'Y'
quadratic_equation_matcher = re.compile(r'(-?\d+)x\^2 ([+-]\d+)x ([+-]\d+)')
while gonext == 'Y' or gonext == 'y' :
    quadratic_equation = input('type equation in the format ax^2+bx+c \n')
    matches = quadratic_equation_matcher.match(quadratic_equation)
    a = int(matches.group(1))
    b = int(matches.group(2))
    c = int(matches.group(3))
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {0} and {1}'.format(sol1,sol2))
    gonext = input('do you wish to continue? y/n \n')
print("finished")
