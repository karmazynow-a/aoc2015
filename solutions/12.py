#AoC2015 day1 part2


floor = 0
basement = 0

with open("output") as f:
	while True:
		basement +=1;
		c = f.read(1)
		if c == '(':
			floor = floor + 1
		elif c == ')':
			floor = floor - 1
		else:
			break
		if floor == -1:
			break

print basement
