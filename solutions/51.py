#AoC2015 day5 part1

def is_nice (s):
	con1 = 0
	con2 = False

	vowels = 'aeiou'
	excluded = 'ab,cd,pq,xy'

	for x in range (0, len(s)-1):
		if s[x:x+2] in excluded: return False
		if s[x] in vowels: con1+=1
		if s[x] == s[x+1]: con2 = True

	if s[-1] in vowels: con1+=1

	if con1>2 and con2 == True: 
		return True
	else: return False

suma = 0

with open("input") as f:
	#for i in range (0,8):
	for line in f:
		
		#line = f.readline()
		if not line: break		
		if is_nice(line.strip())==True: suma+=1

print suma

