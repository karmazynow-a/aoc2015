#AoC2015 day5 part2

def is_nice (s):
	
	con1 = False
	con2 = False

	for x in range (0, len(s)):
		if s[x:x+2] in s[x+2:]: con1 = True
	for x in range (0, len(s)-2):
		if s[x] == s[x+2]: con2 = True

	if con1==True & con2 == True: 
			print s, con1, con2
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

