import time
import random
import statistics
import string
import matplotlib.pyplot as plt
from Algoritms import line, binary, hash_set, binary_fast

# ==============================================================================
# СЛОВАРЬ ДЛЯ ГЕНЕРАЦИИ ДАННЫХ
# ==============================================================================
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
    "идти", "бежать", "смотреть", "слушать", "говорить", "писать", "читать", "думать",
    "программа", "код", "разработка", "тестирование", "отладка", "компиляция", "интерпретация",
    "переменная", "константа", "функция", "процедура", "модуль", "пакет", "библиотека",
    "интерфейс", "класс", "объект", "наследование", "инкапсуляция", "полиморфизм",
    "база", "данные", "таблица", "запрос", "индекс", "ключ", "значение", "запись",
    "поле", "строка", "столбец", "схема", "транзакция", "коммит", "откат", "блокировка",
    "сеть", "протокол", "сервер", "клиент", "запрос", "ответ", "соединение", "порт",
    "адрес", "маршрут", "пакет", "кадр", "поток", "процесс", "нить", "планировщик",
    "память", "кэш", "буфер", "стек", "куча", "указатель", "ссылка", "адрес",
    "файл", "каталог", "путь", "диск", "раздел", "том", "монтирование", "размонтирование",
    "чтение", "запись", "открытие", "закрытие", "создание", "удаление", "копирование",
    "перемещение", "переименование", "архив", "сжатие", "распаковка", "шифрование",
    "дешифрование", "хеш", "подпись", "сертификат", "ключ", "алгоритм", "протокол"
]


def generate_random_word(length=6):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_data(n_words: int, m_stops: int) -> tuple[str, list[str]]:
    stops = []
    available_words = WORD_POOL.copy()
    random.shuffle(available_words)

    for i in range(m_stops):
        if i < len(available_words):
            stops.append(available_words[i])
        else:
            stops.append(f"stop{generate_random_word(5)}")

    text_words = []
    all_words = WORD_POOL + [f"word{generate_random_word(5)}" for _ in range(1000)]

    for _ in range(n_words):
        if random.random() < 0.7 and stops:
            text_words.append(random.choice(stops))
        else:
            text_words.append(random.choice(all_words))

    return " ".join(text_words), stops


def measure_time(func, text: str, stops: list[str], repeats: int = 5) -> float:
    # Прогрев
    for _ in range(3):
        result = func(text, stops)
    assert result is not None or result == ""

    # Замеры
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = func(text, stops)
        end = time.perf_counter()
        times.append(end - start)
        _ = len(result)  # Используем результат, чтобы оптимизатор не выкинул код

    return statistics.median(times)


def plot_results(results: list[dict]):
    """Автоматически строит и сохраняет график по результатам замеров"""
    words_list = [r['words'] for r in results]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1. Логарифмический график (показывает асимптотику)
    ax1.plot(words_list, [r['binary'] for r in results], marker='s', label='binary (O(N·log M))', linewidth=2,
             color='orange')
    ax1.plot(words_list, [r['binary_fast'] for r in results], marker='v', label='binary_fast (bisect/C)', linewidth=2,
             linestyle='--', color='green')
    ax1.plot(words_list, [r['hash_set'] for r in results], marker='^', label='hash_set (O(N+M))', linewidth=2,
             color='blue')

    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Количество слов (N)', fontweight='bold')
    ax1.set_ylabel('Время (секунды)', fontweight='bold')
    ax1.set_title('Логарифмическая шкала\n(прямые линии = степенная зависимость)', fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(words_list)
    ax1.set_xticklabels([f"{w:,}".replace(',', ' ') for w in words_list], rotation=45, ha='right', fontsize=9)

    # 2. Линейный график (показывает реальный разрыв в скорости)
    ax2.plot(words_list, [r['binary'] for r in results], marker='s', label='binary', linewidth=2, color='orange')
    ax2.plot(words_list, [r['binary_fast'] for r in results], marker='v', label='binary_fast', linewidth=2,
             linestyle='--', color='green')
    ax2.plot(words_list, [r['hash_set'] for r in results], marker='^', label='hash_set', linewidth=2, color='blue')

    ax2.set_xlabel('Количество слов (N)', fontweight='bold')
    ax2.set_ylabel('Время (секунды)', fontweight='bold')
    ax2.set_title('Линейная шкала\n(виден реальный отрыв hash_set)', fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(words_list)
    ax2.set_xticklabels([f"{w:,}".replace(',', ' ') for w in words_list], rotation=45, ha='right', fontsize=9)

    plt.tight_layout()
    plt.savefig('benchmark_graph.png', dpi=200, bbox_inches='tight', facecolor='white')
    plt.show()
    print("✅ График успешно сохранён как 'benchmark_graph.png'")


def main():
    # Примечание: Алгоритм 'line' исключён из замеров на больших размерах,
    # так как его сложность O(N·M) приводит к квадратичному росту времени,
    # что делает замеры непрактично долгими.

    sizes = [12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400]

    print(f"{'bytes':>12} | {'words':>8} | {'stops':>8} | {'binary':>12} | {'hash_set':>12} | {'binary_fast':>12}")
    print("-" * 95)

    results = []

    for n_words in sizes:
        m_stops = max(1, n_words // 10)
        text, stops = generate_data(n_words, m_stops)
        bytes_count = len(text.encode('utf-8'))

        print(f"Замер для {n_words:>7} слов, {len(stops):>4} стоп-слов...", end=" ")

        t_bin = measure_time(binary, text, stops)
        t_set = measure_time(hash_set, text, stops)
        t_fast = measure_time(binary_fast, text, stops)

        print("Готово.")
        print(
            f"{'':12}   {bytes_count:>12} | {n_words:>8} | {len(stops):>8} | {t_bin:>12.6f} | {t_set:>12.6f} | {t_fast:>12.6f}")

        results.append({
            'bytes': bytes_count,
            'words': n_words,
            'stops': len(stops),
            'binary': t_bin,
            'hash_set': t_set,
            'binary_fast': t_fast
        })

    print("\n✅ Бенчмаркинг завершён! Построение графика...")

    # Вывод финальной статистики
    last = results[-1]
    print("\n" + "=" * 60)
    print(f"📊 ИТОГ при N={last['words']:,}, M={last['stops']:,}:")
    print(f"   hash_set:      {last['hash_set']:.4f} сек (самый быстрый)")
    print(
        f"   binary_fast:   {last['binary_fast']:.4f} сек (быстрее ручного binary в {last['binary'] / last['binary_fast']:.1f} раз)")
    print(f"   binary:        {last['binary']:.4f} сек")
    print("=" * 60)

    # Автоматическая отрисовка
    plot_results(results)


if __name__ == "__main__":
    main()
