def selection(seq, i):
	if i == 0: return
	selection(seq, i - 1)
	index = i - 1
	min = 10000
	for j in range(i - 1, len(a)):
		if min > a[j]:
			min = a[j]
			index = j

	a[index], a[i - 1] = a[i - 1], a[index]

a = [2, 3, 5, 4, 7, 8, 6, 13, 21, 15, 16, 32, 31, 54, 23]
selection(a, len(a) - 1)
print a