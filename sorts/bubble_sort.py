def bubble_sort(a: list) -> list:
    n = len(a)
    for i in range(1, n):
        for j in range(1, n-i+1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a

a = [2, 5, -3, 4, 3, 21, 11, 1, 153, 0]
print(bubble_sort(a))