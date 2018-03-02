#AoC2015 day3 part2
#czytają instrukcje na zmianę


def go (c, a):
	if c == '^': a[0]+=1
	if c == 'v': a[0]-=1 
	if c == '>': a[1]+=1
	if c == '<': a[1]-=1
	#return a

a = [0,0] #pion, poziom
b = [0,0]
llist = ['0,0']
presents = {
	'0,0':2,
}
counter = 1

with open("input") as f:
	while True:
		s = f.read(1)
		rs = f.read(1)
		if not s: break	
		if not rs: break		
		go (s,a)
		go (rs,b)
		x = ','.join(str(i) for i in a)
		y = ','.join(str(i) for i in b)

		if x not in presents:
			presents[x] = 1
			counter +=1
		else:
			presents[x]+=1
		if y not in presents:
			presents[y] = 1
			counter +=1
		else:
			presents[y]+=1

print counter
		

