def insertion(seq, i):
	if i == 0: return
	insertion(seq, i - 1)

	key = a[i]
	while i >= 0 and a[i - 1] > key:
		a[i - 1], a[i] = a[i], a[i - 1]
		i -= 1


a = [2, 3, 5, 4, 7, 8, 6]
print insertion(a, len(a) - 1)
print a
