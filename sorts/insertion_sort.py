def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

a = [2, 5, -3, 4, 3, 21, 11, 1, 153, 0]
print(insertion_sort(a))