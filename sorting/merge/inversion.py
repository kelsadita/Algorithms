# A version of inversions pair finding algorithm designed on the basis of merge sort algorithm
# Courtesy : Tim Roughgarden (coursera: Algorithm design and analysis 1)

import math
def merge_sort(a, p, r):
	if p < r:
		q = int(math.floor((p + r) / 2))
		
		merge_sort(a, p, q)
		merge_sort(a, q + 1, r)
		
		if q != len(a) - 1:
			merge(a, p, q, r)

def merge(a, p, q, r):

	# creating left and right sub-arrays
	left = a[p:q+1]
	right = a[q+1:r+1]

	# to maintain sentinel (you need to feel it!)
	# the logic can be understood through the program flow
	left.append(100000000)
	right.append(100000000)

	
	# Dunno but removing this gives array index out of bound
	if r == len(a):
		r = r - 1
	
	# comparing and merging routine
	i = 0
	j = 0

	for k in range(p, r + 1):
		if left[i] <= right[j]:
			a[k] = left[i]
			i += 1
		else:
			a[k] = right[j]
			j += 1


#a = [22, 11, 23, 21, 1, 2]
a = [5, 3, 4, 8, 2,1, 4, 8, 9,10, 45,34, 21, 55, 67, 89, 31]

merge_sort(a, 0, len(a))
print a