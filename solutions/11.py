#AoC2015 day1 part1


floor = 0

with open("output") as f:
	while True:
		c = f.read(1)
		if c == '(':
			floor = floor + 1
		elif c == ')':
			floor = floor - 1
		else:
			break

print floor
