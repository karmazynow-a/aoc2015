#AoC2015 day3 part1


def go (c, a):
	if c == '^': a[0]+=1
	if c == 'v': a[0]-=1 
	if c == '>': a[1]+=1
	if c == '<': a[1]-=1
	#return a

a = [0,0] #pion, poziom
llist = ['0,0']
counter = 1

with open("input") as f:
	while True:
		c = f.read(1)
		if not c: break		
		go (c,a)
		#print a
		x = ','.join(str(i) for i in a)
		if x not in llist:
			llist.append(x)
			#print llist
			counter+=1

print counter
		

