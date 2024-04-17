"""AoC Program 24 - 1a"""

import sys
import re

input_txt = open(sys.argv[1]).read().strip()


class Halistone:
    def __init__(self, line):
        """Parse the line with position and velocity."""
        x,y,z,vx,vy,vz = map(int, re.findall(r"-?\d+",line))
        self.p = [x,y,z]
        self.v = [vx,vy,vz]
    def line_intersection(self, next_line):
        """Find intersection current line with next line."""
        x,y,_ = self.p
        vx,vy,_ = self.v
        line1 = ((x,y), (x+vx, y+vy))
        x,y,_ = next_line.p
        vx,vy,_ = next_line.v
        line2 = ((x,y), (x+vx, y+vy))
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None, None

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        if self.isInFuture(x) and next_line.isInFuture(x):
            return x, y
        return None, None
    def isInFuture(self, nX):
        x = self.p[0]
        vx = self.v[0]
        return (nX - x)/vx >= 0
    
    
result = 0
halistones = [Halistone(l) for l in input_txt.splitlines()]
ta = (7, 27) if len(halistones) < 10 else (200000000000000,400000000000000)
for i in range(len(halistones)-2):
    for j in range(i+1, len(halistones)):
        x, y = halistones[i].line_intersection(halistones[j])
        if x:
            if ta[0]<=x<=ta[1] and ta[0]<=y<=ta[1]:
                result += 1
print(result)
                
