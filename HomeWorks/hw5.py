def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 7
    result = binary_search(sorted_list, target_value)

    if result != -1:
        print(f"Element {target_value} found at index {result}.")
    else:
        print(f"Element {target_value} not found in the list.")