def max_per(m):
	indices = set(m.values())
	old_m = m.copy()

	for i in m.keys():
		if i not in indices:
			del m[i]

	
	if m == old_m:
		print m.keys()
	else:
		max_per(m)

m = {0:2, 1:2, 2:0, 3:5, 4:3, 5:5, 6:7, 7:4}
print max_per(m)