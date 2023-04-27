
# import modules

# O(n) Big O notaction
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers


# Binary Search
# Returns index of x in arr if present, else -1
def binary_searchs(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# Iterative Binary Search


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


# function main
def main() -> None:
    # call
    arr = [2, 5, 8, 9, 10, 25, 45]
    x = 10

    res = binary_search(arr, x)
    print(f"Element index ", str(res))


if __name__ == '__main__':
    main()
