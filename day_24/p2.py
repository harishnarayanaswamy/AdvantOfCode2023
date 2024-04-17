"""AoC Program 24 - 1b"""

import sys
import re
from sympy import Symbol, solve_poly_system


class Hailstone:
	def __init__(self, line):
		x,y,z,vx,vy,vz = map(int, re.findall(r"-?\d+",line))
		self.p = [x,y,z]
		self.v = [vx,vy,vz]

def rock_position(hailstones):
    x,y,z,vx,vy,vz = (Symbol(c) for c in "x,y,z,vx,vy,vz".split(','))
    p = [x,y,z]
    v = [vx,vy,vz]
    vars = [*p, *v]
    eqs = []
    for i, hs in enumerate(hailstones[:3]):
        t = Symbol(f"t_{i}")
        for j in range(3):
            eqs.append(p[j]+v[j]*t - (hs.p[j] + hs.v[j]*t))
        vars.append(t)
    return int(sum(solve_poly_system(eqs, vars)[0][:3]))


input_txt = open(sys.argv[1]).read().strip()
halistones = [Hailstone(l) for l in input_txt.splitlines()]
print(rock_position(halistones))
              