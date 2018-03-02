#AoC2015 day2 part2

def smallest (l=0,w=0,h=0):
	a = 2*l + 2*w
	b = 2*l + 2*h
	c = 2*w + 2*h
	if a < b:
		if c < a: return c
		else: return a
	else:
		if c < b: return c
		else: return b

def surface (l=0,w=0,h=0):
	return l*w*h + smallest (l,w,h)


suma = 0

with open("input") as f:
	for line in f:
		
		if not line: break		
	
		a=line.strip().split("x")
		suma = suma + surface (int(a[0]),int(a[1]),int(a[2]))

print suma

