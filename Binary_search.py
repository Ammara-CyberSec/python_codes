# Binary Search
def binary_search(arr,target):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = (low + high)//2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return -1
numbers = [10,23,34,45,52,55,65,78,90]
target = 45
result =binary_search(numbers,target)
if result != -1:
	print(f"Found at index {result}")
else:
	print("Not found")






# Binary Search with Recursion
def binary_search(arr,low,high,target):
	if low > high:
		return -1
	mid = (low + high)//2
	if arr[mid] == target:
		return mid
	elif arr[mid] < target:
		return binary_search(arr,mid +1,high,target)
	else:
		return binary_search(arr,low,mid - 1,target)
num = [10,23,34,45,56,62,64,66,78,88,90]
target = 88
result = binary_search(num,0,len(num)-1,target)
if result != -1:
	print(f"Found at index {result}")
else:
	print("Not found")
	