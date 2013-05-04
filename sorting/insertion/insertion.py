def insertion(a):
	for j in xrange(1, len(a)):
		key = a[j]
		i   = j - 1
		while i >= 0 and a[i] > key:
			a[i + 1] = a[i]
			a[i] = key
			i = i - 1
	return a

print insertion([2, 3, 5, 4, 7, 8, 6])
