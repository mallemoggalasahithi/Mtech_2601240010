import time
from random import randint

from src.merge_sort import merge_sort


def benchmark():
    sizes = [1000, 5000, 10000]

    print("MERGE SORT PERFORMANCE")
    print("-" * 40)

    for size in sizes:
        numbers = [randint(1, 100000) for _ in range(size)]

        start = time.perf_counter()

        merge_sort(numbers)

        end = time.perf_counter()

        print(
            f"Input size: {size:>6} | "
            f"Time: {end - start:.6f} seconds"
        )


if __name__ == "__main__":
    benchmark()
    