def ternary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
    
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            return mid1 
        if arr[mid2] == target:
            return mid2 

        if target < arr[mid1]:
            high = mid1 - 1 
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1 
            high = mid2 - 1

    return -1


# Example usage
array = [10, 20, 30, 40, 50, 60, 70]
target = int(input("Enter the number to search: "))

index = ternary_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
