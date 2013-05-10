num_inversions = 0
def merge(i, j, middle):
    global num_inversions
    if j - i == 1:
        left  = [arr[i]]
        right = [arr[j]] 
    else:
        left  = arr[i:middle+1]
        right = arr[middle+1:j+1] 
  
    left.append(10000000)
    right.append(10000000)
 
    #print "-------------------------------"
    #print "left: ",left
    #print "right ",right
    #print "-------------------------------"
 
    p, q = 0, 0
 
    for index in range(i, j+1):
        if left[p] < right[q]:
            arr[index] = left[p]
            p += 1
        else:
            arr[index] = right[q]
            num_inversions += (len(left) - p - 1)
            q += 1
 
def mergesort(a, b):
    if a < b:
        #following step is important as it preserves the sanity of the indices
        middle = a + (b - a)/ 2 
        mergesort(a, middle)
        mergesort(middle + 1, b)
        
        merge(a, b, middle)
 
 
if __name__ == "__main__":
 
    f = open('IntegerArray.txt', 'r')
    arr = f.read().splitlines()
    arr = [int(a) for a in arr]
    mergesort(0, len(arr) - 1);
 
    #print "Sorted array: \n"
    #print arr
 
    print "Number of inversions : ", num_inversions