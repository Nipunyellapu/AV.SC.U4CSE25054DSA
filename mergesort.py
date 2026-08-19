def merge_sort(arr):

    
    if len(arr) <= 1:
        return arr

    
    mid = len(arr) // 2

    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    
    return merge(left, right)

def merge(left, right):

    result = []

    i = 0
    j = 0


    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))


arr = merge_sort(arr)

print("Sorted array:", arr)
