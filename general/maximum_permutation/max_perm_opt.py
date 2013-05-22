def max_perm(m):
	n = len(m)
	a = range(n)
	count = [0] * n
	for i in m:
		count[i] += 1
	q = [i for i in a if count[i] == 0]
	while q:
		i = q.pop()
		a.remove(i)
		count[m[i]] -= 1
		if count[m[i]] == 0:
			q.append(m[i])
	return a


m = [2, 2, 0, 5, 3, 5, 7, 4]
print max_perm(m)