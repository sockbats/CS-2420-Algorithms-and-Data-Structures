from random import seed, sample
from time import perf_counter
from math import sqrt


def generate_data():
    data_size = 1000000
    seed("seed")
    data = sample(range(3 * data_size), data_size)
    data.sort()
    yield data


def linear_search(lyst, target):
    for i in lyst:
        if i == target:
            return True
    return False


def binary_search(lyst, target):
    while True:
        midpoint = len(lyst) // 2
        if lyst[midpoint] == target:
            return True
        if target < lyst[midpoint]:
            lyst = lyst[:midpoint]
        else:
            lyst = lyst[midpoint:]
        if len(lyst) == 1:
            if lyst[0] == target:
                return True
            else:
                return False


def jump_search(lyst, target):
    jump_distance = round(sqrt(len(lyst)))
    current_index = 0
    while current_index + jump_distance <= len(lyst):
        previous_index = current_index
        current_index += jump_distance
        if current_index >= len(lyst):
            for i in lyst[previous_index:current_index+1]:
                if i == target:
                    return True
            return False
        if lyst[current_index] > target:
            for i in lyst[previous_index:current_index+1]:
                if i == target:
                    return True
    return False


def search_beginning():
    data = next(generate_data())
    target = data[0]

    start = perf_counter()
    assert linear_search(data, target)
    linear_time = perf_counter() - start

    start = perf_counter()
    assert binary_search(data, target)
    binary_time = perf_counter() - start

    start = perf_counter()
    assert jump_search(data, target)
    jump_time = perf_counter() - start

    return linear_time, binary_time, jump_time


def search_middle():
    data = next(generate_data())
    target = data[len(data) // 2]

    start = perf_counter()
    assert linear_search(data, target)
    linear_time = perf_counter() - start

    start = perf_counter()
    assert binary_search(data, target)
    binary_time = perf_counter() - start

    start = perf_counter()
    assert jump_search(data, target)
    jump_time = perf_counter() - start

    return linear_time, binary_time, jump_time


def search_end():
    data = next(generate_data())
    target = data[-1]

    start = perf_counter()
    assert linear_search(data, target)
    linear_time = perf_counter() - start

    start = perf_counter()
    assert binary_search(data, target)
    binary_time = perf_counter() - start

    start = perf_counter()
    assert jump_search(data, target)
    jump_time = perf_counter() - start

    return linear_time, binary_time, jump_time


def search_not_exist():
    data = next(generate_data())
    target = -1

    start = perf_counter()
    assert not linear_search(data, target)
    linear_time = perf_counter() - start

    start = perf_counter()
    assert not binary_search(data, target)
    binary_time = perf_counter() - start

    start = perf_counter()
    assert not jump_search(data, target)
    jump_time = perf_counter() - start

    return linear_time, binary_time, jump_time


def main():
    searching = ("Linear Search", "Binary Search", "Jump Search Time")
    beginning_search = search_beginning()
    middle_search = search_middle()
    end_search = search_end()
    not_exist_search = search_not_exist()

    print("\nSearch for Beginning:")
    for i in range(3):
        print(f"{searching[i]} Time: {beginning_search[i]}")
    print("\nSearch for Middle:")
    for i in range(3):
        print(f"{searching[i]} Time: {middle_search[i]}")
    print("\nSearch for End:")
    for i in range(3):
        print(f"{searching[i]} Time: {end_search[i]}")
    print("\nSearch for Value not in range:")
    for i in range(3):
        print(f"{searching[i]} Time: {not_exist_search[i]}")


if __name__ == '__main__':
    main()
