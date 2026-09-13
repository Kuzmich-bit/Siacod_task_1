import time
import random
import statistics
from Algoritms import line, binary, hash_set, binary_fast

WORD_POOL = [
    "слово", "текст", "данные", "алгоритм", "поиск", "список", "массив", "строка",
    "число", "значение", "ключ", "элемент", "узел", "дерево", "граф", "таблица",
    "функция", "метод", "класс", "объект", "переменная", "константа", "параметр",
    "результат", "вывод", "ввод", "операция", "вычисление", "проверка", "условие",
    "цикл", "итерация", "шаг", "проход", "сравнение", "сортировка", "фильтрация",
    "удаление", "добавление", "изменение", "копирование", "перемещение", "поиск",
    "начало", "конец", "середина", "граница", "диапазон", "интервал", "отрезок",
    "мама", "папа", "кот", "собака", "дом", "окно", "дверь", "стол", "стул",
    "книга", "ручка", "тетрадь", "школа", "учитель", "ученик", "урок", "перемена",
    "вода", "огонь", "земля", "небо", "солнце", "луна", "звезда", "облако",
    "быстрый", "медленный", "большой", "маленький", "новый", "старый", "хороший",
    "идти", "бежать", "смотреть", "слушать", "говорить", "писать", "читать", "думать"
]


def generate_data(n_words: int, m_stops: int) -> tuple[str, list[str]]:

    actual_m_stops = min(m_stops, len(WORD_POOL) // 2)

    stops = random.sample(WORD_POOL, actual_m_stops)

    text_words = []
    for _ in range(n_words):
        if random.random() < 0.7:
            text_words.append(random.choice(WORD_POOL))
        else:
            available = [w for w in WORD_POOL if w not in stops]
            text_words.append(random.choice(available))

    text = " ".join(text_words)
    return text, stops


def measure_time(func, text: str, stops: list[str], repeats: int = 5) -> float:
    for _ in range(3):
        result = func(text, stops)
    assert result is not None or result == ""

    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = func(text, stops)
        end = time.perf_counter()
        times.append(end - start)
        _ = len(result)
    return statistics.median(times)


def main():
    sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800]

    print("Генерация данных и замеры...")
    print(f"{'bytes':>12} | {'words':>8} | {'stops':>8} | {'line':>12} | {'binary':>12} | {'hash_set':>12} | {'binary_fast':>12}")
    print("-" * 95)

    results = []

    for n_words in sizes:
        m_stops = max(1, n_words // 10)
        text, stops = generate_data(n_words, m_stops)
        bytes_count = len(text.encode('utf-8'))
        t_lin = measure_time(line, text, stops)
        t_bin = measure_time(binary, text, stops)
        t_set = measure_time(hash_set, text, stops)
        t_fast = measure_time(binary_fast, text, stops)

        print(f"{bytes_count:>12} | {n_words:>8} | {len(stops):>8} | {t_lin:>12.6f} | {t_bin:>12.6f} | {t_set:>12.6f} | {t_fast:>12.6f}")

        results.append({
            'bytes': bytes_count,
            'words': n_words,
            'stops': len(stops),
            'line': t_lin,
            'binary': t_bin,
            'hash_set': t_set,
            'binary_fast': t_fast
        })
    return results

if __name__ == "__main__":
    main()