#AoC2015 day2 part1

def smallest (l=0,w=0,h=0):
	a = l*w
	b = l*h
	c = w*h
	if a < b:
		if c < a: return c
		else: return a
	else:
		if c < b: return c
		else: return b

def surface (l=0,w=0,h=0):
	return 2*l*w + 2*w*h + 2*h*l + smallest (l,w,h)


suma = 0

with open("input") as f:
	for line in f:
		
		if not line: break		
	
		a=line.strip().split("x")
		suma = suma + surface (int(a[0]),int(a[1]),int(a[2]))

print suma

