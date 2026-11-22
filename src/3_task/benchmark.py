import json
import random
import time
import tracemalloc
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


def measure(func, data, repeats=3):
    times = []
    memories = []

    for _ in range(repeats):
        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(data)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        times.append((end_time - start_time) * 1000)
        memories.append(peak / 1024)

    return sum(times) / len(times), sum(memories) / len(memories), result


def main():
    print("=" * 70)
    print(f"{'Размер':<10} | {'Метод':<15} | {'Время (мс)':<12} | {'Память (КБ)':<12} | {'Буферов'}")
    print("=" * 70)

    for count in [100, 500, 1000, 3000, 5000]:
        data = generate_data(count)

        t_heap, m_heap, res_heap = measure(solve, data)

        t_etalon, m_etalon, res_etalon = measure(solve_etalon, data)

        match = "Ok" if res_heap[1] == res_etalon[1] else "No"

        print(f"{count:<10} | {'Куча':<15} | {t_heap:<12.3f} | {m_heap:<12.2f} | {res_heap[1]} {match}")
        print(f"{'':<10} | {'Эталон':<15} | {t_etalon:<12.3f} | {m_etalon:<12.2f} | {res_etalon[1]}")

        speedup = t_etalon / t_heap if t_heap > 0 else 0
        print(f"{'':<10} | {'Ускорение':<15} | {speedup:.1f}x быстрее")
        print("-" * 70)


if __name__ == "__main__":
    main()