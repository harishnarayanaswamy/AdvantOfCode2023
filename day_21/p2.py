import numpy as np
import sys
P = complex
class Grid:
	def __init__(self, input):
		self.size = len(input.splitlines())
		self.grid = set()
		self.positions = set()
		for y, l in enumerate(input.splitlines()):
			for x, v in enumerate(l):
				if v == '#':
					self.grid.add(P(x,y))
				if v == 'S':
					self.positions.add(P(x,y))
	def step(self):
		newPos = set()
		for p in self.positions:
			for d in (1,-1,1j,-1j):
				if self.wrap(p+d) not in self.grid:
					newPos.add(p+d)
		self.positions = newPos
	def wrap(self, p):
		return P(p.real%self.size, p.imag%self.size)

def main(input):
	g = Grid(input)
	# f(x) = how many squares are visited at time 65 + 131*x
	X,Y = [0,1,2], []
	target = (26501365 - 65)//131
	for s in range(65 + 131*2 + 1):
		if s%131 == 65:
			Y.append(len(g.positions))
		if s == 64:
			p1 = len(g.positions)
		g.step()
	poly = np.rint(np.polynomial.polynomial.polyfit(X,Y,2)).astype(int).tolist()
	return p1, sum(poly[i]*target**i for i in range(3))

inp = open(sys.argv[1]).read().strip()
results = main(inp)
print(results)