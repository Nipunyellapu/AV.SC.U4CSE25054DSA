def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


n = int(input("Enter the number of elements: "))
print("Enter the elements:")
arr = []
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to be found: "))

if arr != sorted(arr):
    print("Array is not sorted")
    arr.sort()
    print(f"Sorted array: {arr}")

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result} in the sorted array")
else:
    print("Element not found in the array")
