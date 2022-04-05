# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  if x < arr[l] or x > arr[r]:
    return -1 
  m = l +int((l+r)/2)
  if arr[m]==x:
    return m
  if arr[m]<x:
    binarySearch(arr, m+1, r, x)
  else:
    binarySearch(arr, l, m-1, x)    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")