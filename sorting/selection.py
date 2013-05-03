def selection(a):
	index = 0
	for j in xrange(0, len(a)):
		minq = 10000
		for i in xrange(j, len(a)):
			if minq > a[i]:
				minq = a[i]
				index = i
		a[j], a[index] = a[index], a[j]
		
	return a

print selection([2, 3, 5, 4, 7, 8, 6, 1, 23, 21, 19, 15])