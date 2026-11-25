import random
import time
import statistics
from ReusingBuffersDuringRendering import solve, solve_etalon


def generate_data(count, seed=42):
    random.seed(seed)
    max_time = max(count * 10, 100)
    intervals = []
    for i in range(count):
        start = random.randint(0, max_time - 1)
        end = random.randint(start + 1, max_time)
        intervals.append((start, end, f"res_{i}"))
    return intervals


def measure(func, data, repeats=7):
    for _ in range(3):
        func(data)

    times = []
    checksum = 0

    for _ in range(repeats):
        t0 = time.perf_counter()
        result = func(data)
        t1 = time.perf_counter()

        for res_id, buf_num in result[0]:
            checksum += buf_num

        times.append((t1 - t0) * 1e6)

    median_us = statistics.median(times)
    return median_us, checksum

def main():
    sizes = [100, 200, 400, 800, 1600, 3200, 6400]

    rows = []
    for n in sizes:
        data = generate_data(n)
        t_heap, _ = measure(solve, data)
        t_et, _ = measure(solve_etalon, data)
        rows.append((n, t_heap, t_et))
        print(f"n={n:<6} куча={t_heap:>10.1f} мкс  эталон={t_et:>10.1f} мкс  "
              f"ускорение={t_et/t_heap:>6.1f}x")



if __name__ == "__main__":
    main()