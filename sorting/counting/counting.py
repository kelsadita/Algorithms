from collections import defaultdict

def counting_sort(a):
	b, c = [], defaultdict(list)
	for x in a:
		c[x].append(x)
	for k in range(min(c), max(c) + 1):
		b.extend(c[k])
	return b

a = [2, 3, 1, 4, 5, 12, 10]

print counting_sort(a)