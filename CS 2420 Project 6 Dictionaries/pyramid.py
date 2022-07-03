import sys
from time import perf_counter
from hashmap import HashMap
calls = 0
cache = HashMap()
cache_calls = 0


def get_weight(row, column=None):
    if column is None:
        # part_2 = open("part2.txt", "w")
        part_3 = open("part3.txt", "w")
        start = perf_counter()
        for i in range(row):
            for j in range(i + 1):
                # print(f"{weight_on(i, j):.2f}", end=" ")
                # part_2.write(f"{weight_on(i, j):.2f} ")
                part_3.write(f"{weight_on(i, j):.2f} ")
            # print()
            # part_2.write("\n")
            part_3.write("\n")
        time_elapsed = perf_counter() - start
        # print(f"\nElapsed time: {time_elapsed} seconds\nFunction Calls: {calls}")
        # part_2.write(f"\nElapsed time: {time_elapsed} seconds\nFunction Calls: {calls}")
        part_3.write(f"\nElapsed time: {time_elapsed} seconds\nFunction Calls: {calls}\nCache Calls: {cache_calls}")
        # part_2.close()
        part_3.close()
    else:
        print(f"{weight_on(row, column):.2f}")


def weight_on(row, column):
    global calls
    global cache
    global cache_calls
    calls += 1
    try:
        temp = cache[(row, column)]
        cache_calls += 1
        return temp
    except KeyError:
        pass
    if row == 0 and column == 0:
        weight = 0.0
        cache[(row, column)] = weight
        return weight
    elif row == 1:
        weight = 100.0
        cache[(row, column)] = weight
        return weight
    elif column == 0:
        weight = (weight_on(row - 1, 0) + 200) / 2
        cache[(row, column)] = weight
        return weight
    elif column == row:
        weight = (weight_on(row - 1, column - 1) + 200) / 2
        cache[(row, column)] = weight
        return weight
    else:
        weight = ((weight_on(row - 1, column - 1) + 200) / 2) + ((weight_on(row - 1, column) + 200) / 2)
        cache[(row, column)] = weight
        return weight


def main():
    """
    If there are args, will run to a certain amount of lines
    If there are no args, will run what is under except IndexError.
    """
    try:
        get_weight(int(sys.argv[1]))
    except IndexError:
        """If there are no args, will run this code. 
        If ran from console, elapsed time will be incorrect"""
        # get_weight(5, 5)
        # get_weight(2, 1)
        # get_weight(7)
        get_weight(20)
        # get_weight(5)
        # get_weight(500, 250)
        pass


if __name__ == '__main__':
    main()
