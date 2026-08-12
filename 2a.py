def linear_search(arr,target):
    n = len(arr)
    for i in range (n):
        if (arr[i] == target):
            return i
    return -1

n = int(input("Enter the number of elements:"))
arr = []
print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))
target = int(input("Enter the element to be found:"))
result = linear_search(arr,target)

if(result != -1):
    print(f"Element {target} found at {result} index")
else:
    print("Element not found in the given array")

    
    
    
        
