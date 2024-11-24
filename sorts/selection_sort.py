def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(0, n):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


a = [2, 5, -3, 4, 3, 21, 11, 1, 153, 0]
print(selection_sort(a))