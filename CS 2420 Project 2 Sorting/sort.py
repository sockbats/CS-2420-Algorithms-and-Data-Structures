from random import seed, sample
from time import perf_counter


def quicksort(lyst):
    quicksorth(lyst, 0, len(lyst) - 1)
    return lyst


def quicksorth(lyst, left, right):
    if left >= right:
        return
    pivot = partition(lyst, left, right)
    quicksorth(lyst, left, lyst.index(pivot) - 1)
    quicksorth(lyst, lyst.index(pivot) + 1, right)


def partition(lyst, left=0, right=-1):
    pivot = lyst[right]
    j = left - 1
    for i in range(left, right):
        if lyst[i] <= pivot:
            j += 1
            lyst[i], lyst[j] = lyst[j], lyst[i]

    lyst[lyst.index(pivot)] = lyst[j + 1]
    lyst[j + 1] = pivot
    return pivot


def mergesort(lyst):
    if len(lyst) > 1:
        midpoint = len(lyst) // 2
        left = lyst[:midpoint]
        right = lyst[midpoint:]

        mergesort(left)
        mergesort(right)

        left_i, right_i, list_i = 0, 0, 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                lyst[list_i] = left[left_i]
                left_i += 1
            else:
                lyst[list_i] = right[right_i]
                right_i += 1
            list_i += 1

        while left_i < len(left):
            lyst[list_i] = left[left_i]
            left_i += 1
            list_i += 1

        while right_i < len(right):
            lyst[list_i] = right[right_i]
            right_i += 1
            list_i += 1

    return lyst


def selection_sort(lyst):
    for i in range(len(lyst)):
        minimum = lyst[i]
        for j in lyst[i:]:
            if minimum < j:
                pass
            else:
                minimum = j
        lyst.remove(minimum)
        lyst.insert(0, minimum)
    return lyst[::-1]


def insertion_sort(lyst):
    for i in range(len(lyst) - 1):
        if lyst[i] < lyst[i + 1]:
            pass
        else:
            j = i
            while lyst[j] > lyst[j + 1] and j > -1:
                lyst[j], lyst[j + 1] = lyst[j + 1], lyst[j]
                j -= 1
    return lyst


def is_sorted(lyst):
    lyst2 = lyst.copy()
    lyst2.sort()
    return lyst == lyst2


def main():
    data_size = 10000
    seed("seed")
    data = sample(range(3 * data_size), data_size)
    data_copy = data.copy()
    sorted_data = data.copy()
    sorted_data.sort()

    # print(sorted_data)

    start = perf_counter()
    data = data_copy
    quicksort(data)
    print(f"Quicksort: {perf_counter() - start} seconds")

    start = perf_counter()
    data = data_copy
    mergesort(data)
    print(f"Mergesort: {perf_counter() - start} seconds")

    start = perf_counter()
    data = data_copy
    selection_sort(data)
    print(f"Selection sort: {perf_counter() - start} seconds")

    start = perf_counter()
    data = data_copy
    insertion_sort(data)
    print(f"Insertion sort: {perf_counter() - start} seconds")

    start = perf_counter()
    data = data_copy
    sorted(data)
    print(f"Tim sort: {perf_counter() - start} seconds")


if __name__ == '__main__':
    main()
