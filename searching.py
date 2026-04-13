import json
import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence


def read_data(file_name, field):
    with open(file_name, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    allowed_fields = ["unordered_numbers", "ordered_numbers", "dna_sequence"]
    if field not in allowed_fields:
        return None
    return data[field]


def linear_search(sequence, target):
    positions = []

    for i in range(len(sequence)):
        if sequence[i] == target:
            positions.append(i)

    result = {
        "positions": positions,
        "count": len(positions)
    }
    return result


def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        middle = (left + right) // 2

        if sequence[middle] == target:
            return middle

        if sequence[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


def set_membership(data_set, target):
    if target in data_set:
        return True
    return False


def measure_linear_time(data, target, repeats=100):
    total = 0

    for i in range(repeats):
        start = time.perf_counter()
        linear_search(data, target)
        end = time.perf_counter()
        total += end - start

    avg_time = total / repeats
    return avg_time


def measure_binary_time(data, target, repeats=100):
    total = 0

    for i in range(repeats):
        start = time.perf_counter()
        binary_search(data, target)
        end = time.perf_counter()
        total += end - start

    avg_time = total / repeats
    return avg_time


def measure_set_time(data_set, target, repeats=100):
    total = 0

    for i in range(repeats):
        start = time.perf_counter()
        set_membership(data_set, target)
        end = time.perf_counter()
        total += end - start

    avg_time = total / repeats
    return avg_time


def main():
    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []
    set_times = []

    for size in sizes:
        unordered_data = unordered_sequence(max_len=size)
        ordered_data = ordered_sequence(max_len=size)

        linear_target = unordered_data[-1]
        binary_target = ordered_data[-1]

        linear_time = measure_linear_time(unordered_data, linear_target, 200)
        binary_time = measure_binary_time(ordered_data, binary_target, 200)

        data_set = set(unordered_data)
        set_time = measure_set_time(data_set, linear_target, 200)

        linear_times.append(linear_time)
        binary_times.append(binary_time)
        set_times.append(set_time)

    print("sizes =", sizes)
    print("linear_times =", linear_times)
    print("binary_times =", binary_times)
    print("set_times =", set_times)

    plt.plot(sizes, linear_times, marker="o", label="Linear search")
    plt.plot(sizes, binary_times, marker="o", label="Binary search")
    plt.plot(sizes, set_times, marker="o", label="Set membership")

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Cas behu")
    plt.title("Porovnani casu vyhledavani")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Linear search je nejpomalejsi, protoze prochazi seznam postupne.")
    print("Binary search je rychlejsi, protoze pracuje jen se serazenym seznamem a pulí interval.")
    print("Set membership byva nejrychlejsi, protoze hledani v mnozine je prumerne O(1).")


if __name__ == "__main__":
    main()