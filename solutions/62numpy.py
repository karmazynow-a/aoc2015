#AoC2015 day6 part2

import numpy

size = 1000

matrix = numpy.zeros((size, size), "int")

with open("input") as f:
	for line in f:
		a = line.strip().split(" ")
 
		st = a[-3].split(",")
		ast, bst = int(st[0]), int(st[1])
		fi = a[-1].split(",")
		af, bf = int(fi[0]), int(fi[1])

		if a[-4] == "on": 
			matrix[ast:af+1, bst:bf+1] +=1
		elif a[-4] == "off": 
			matrix[ast:af+1, bst:bf+1] -=1
			matrix[matrix<0]=0
		elif a[-4] == "toggle": 
			matrix[ast:af+1, bst:bf+1] +=2

	print numpy.sum(matrix)

