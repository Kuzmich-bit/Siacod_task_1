from ReusingBuffersDuringRendering import solve, solve_etalon


def get_max_concurrent(intervals):
    events = []
    for s, e, _ in intervals:
        events.append((s, 1))   # +1 ресурс в момент start
        events.append((e, -1))  # -1 ресурс в момент end

    events.sort(key=lambda x: (x[0], x[1]))

    current = 0
    max_c = 0
    for _, delta in events:
        current += delta
        if current > max_c:
            max_c = current
    return max_c


def check_no_overlaps(intervals, assignments):

    buffers = {}
    for s, e, rid in intervals:
        buf = assignments[rid]
        if buf not in buffers:
            buffers[buf] = []
        buffers[buf].append((s, e))

    # Для каждого буфера проверяем его интервалы
    for buf, ivs in buffers.items():
        ivs.sort()  # Сортируем по началу
        for i in range(1, len(ivs)):
            # Если начало следующего меньше конца предыдущего — пересечение!
            if ivs[i][0] < ivs[i-1][1]:
                return False
    return True


def run_test(name, intervals, expected_buffers):
    """Запускает оба решения и проверяет все условия."""
    res_solve, tot_solve = solve(intervals)
    res_etalon, tot_etalon = solve_etalon(intervals)

    ok = True

    # 1. Проверяем, что оба решения дали одинаковый и ожидаемый результат
    if tot_solve != expected_buffers or tot_etalon != expected_buffers:
        ok = False
    if tot_solve != tot_etalon:
        ok = False

    # 2. Сложные проверки (только если вход не пустой)
    if intervals:
        max_c = get_max_concurrent(intervals)
        # Число буферов должно быть равно максимуму одновременно занятых ресурсов
        if tot_solve != max_c:
            ok = False

        # Проверяем отсутствие пересечений у ресурсов одного буфера
        dict_solve = {rid: b for rid, b in res_solve}
        if not check_no_overlaps(intervals, dict_solve):
            ok = False

    status = "OK" if ok else "NOT OK"
    print(f"{status} [{name:<25}] Буферов: {tot_solve} | Ожидалось: {expected_buffers} | Макс. одновременных: {get_max_concurrent(intervals) if intervals else 0}")
    return ok


if __name__ == "__main__":
    print("ЗАПУСК ТЕСТОВ ИЗ ЗАДАНИЯ:")
    print("-" * 80)

    all_passed = True

    # 1. Пустой вход
    all_passed &= run_test("Пустой вход", [], 0)

    # 2. Непересекающиеся (включая касание границ)
    all_passed &= run_test("Непересекающиеся", [
        (0, 5, "A"), (5, 10, "B"), (10, 15, "C")
    ], 1)

    # 3. Полностью перекрывающиеся
    all_passed &= run_test("Полное перекрытие", [
        (0, 10, "A"), (0, 10, "B"), (0, 10, "C")
    ], 3)

    # 4. Вложенность
    all_passed &= run_test("Вложенность", [
        (0, 20, "A"), (5, 15, "B"), (8, 12, "C")
    ], 3)

    # 5. Равные начала
    all_passed &= run_test("Равные начала", [
        (0, 5, "A"), (0, 10, "B"), (0, 15, "C")
    ], 3)

    # 6. Равные окончания
    all_passed &= run_test("Равные окончания", [
        (0, 10, "A"), (5, 10, "B"), (8, 10, "C")
    ], 3)

    # 7. Касание границ (допускает переиспользование)
    all_passed &= run_test("Касание границ", [
        (0, 5, "A"), (5, 10, "B"), (10, 15, "C")
    ], 1)

    # 8. Смешанный сложный случай (из наших прошлых разборов)
    all_passed &= run_test("Смешанный случай", [
        (0, 5, "A"), (3, 8, "B"), (6, 10, "C"), (2, 4, "D"), (7, 9, "E")
    ], 3)

    print("-" * 80)
    if all_passed:
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! МОЖНО СДАВАТЬ.")
    else:
        print("⚠️ ЕСТЬ ПРОВАЛЫ. ПРОВЕРЬ КОД.")