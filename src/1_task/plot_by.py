import matplotlib.pyplot as plt

data = {
    'words': [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200],
    'stops': [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],
    'line': [0.000009, 0.000023, 0.000067, 0.000231, 0.000739, 0.002448, 0.010070, 0.041119, 0.172773, 0.689746],
    'binary': [0.000025, 0.000062, 0.000144, 0.000327, 0.000697, 0.001415, 0.003226, 0.007100, 0.015843, 0.035683],
    'hash_set': [0.000006, 0.000013, 0.000025, 0.000050, 0.000088, 0.000143, 0.000285, 0.000570, 0.001192, 0.002402],
    'binary_fast': [0.000012, 0.000025, 0.000060, 0.000100, 0.000195, 0.000367, 0.000825, 0.001792, 0.004086, 0.008795]
}

# Создаём график с двумя осями Y для лучшего сравнения
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Левый график: логарифмическая шкала (прямые линии)
#ax1.plot(data['words'], data['line'], marker='o', label='line (O(N·M))', linewidth=2.5, markersize=7)
ax1.plot(data['words'], data['binary'], marker='s', label='binary (O(N·log M))', linewidth=2.5, markersize=7)
ax1.plot(data['words'], data['binary_fast'], marker='v', label='binary_fast (bisect/C)', linewidth=2.5, markersize=7, linestyle='--')
ax1.plot(data['words'], data['hash_set'], marker='^', label='hash_set (O(N+M))', linewidth=2.5, markersize=7)

ax1.set_xlabel('Количество слов (N)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Время выполнения (секунды)', fontsize=11, fontweight='bold')
ax1.set_title('Логарифмическая шкала\n(M = N/10 растёт)', fontsize=12, fontweight='bold', pad=15)
ax1.legend(fontsize=9, loc='upper left')
ax1.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xticks(data['words'])
ax1.set_xticklabels([str(w) for w in data['words']], rotation=45, ha='right', fontsize=8)

# Правый график: линейная шкала (виден рост)
#ax2.plot(data['words'], data['line'], marker='o', label='line (O(N·M))', linewidth=2.5, markersize=7, color='red')
ax2.plot(data['words'], data['binary'], marker='s', label='binary (O(N·log M))', linewidth=2.5, markersize=7, color='orange')
ax2.plot(data['words'], data['binary_fast'], marker='v', label='binary_fast (bisect/C)', linewidth=2.5, markersize=7, linestyle='--', color='green')
ax2.plot(data['words'], data['hash_set'], marker='^', label='hash_set (O(N+M))', linewidth=2.5, markersize=7, color='blue')

ax2.set_xlabel('Количество слов (N)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Время выполнения (секунды)', fontsize=11, fontweight='bold')
ax2.set_title('Линейная шкала\n(виден квадратичный рост line)', fontsize=12, fontweight='bold', pad=15)
ax2.legend(fontsize=9, loc='upper left')
ax2.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax2.set_xticks(data['words'])
ax2.set_xticklabels([str(w) for w in data['words']], rotation=45, ha='right', fontsize=8)

plt.tight_layout()
plt.savefig('benchmark_with_growing_M.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()

# Выводим статистику
print("=" * 70)
print("📊 РЕЗУЛЬТАТЫ БЕНЧМАРКИНГА (M растёт пропорционально N)")
print("=" * 70)
print(f"\nПри N={data['words'][-1]}, M={data['stops'][-1]} (M = N/10):")
print(f"  • hash_set:      {data['hash_set'][-1]:.6f} сек ✓ САМЫЙ БЫСТРЫЙ")
print(f"  • binary_fast:   {data['binary_fast'][-1]:.6f} сек")
print(f"  • binary:        {data['binary'][-1]:.6f} сек")
print(f"  • line:          {data['line'][-1]:.6f} сек  САМЫЙ МЕДЛЕННЫЙ")
print(f"\n📈 Ускорение:")
print(f"  ✓ hash_set быстрее line в {data['line'][-1]/data['hash_set'][-1]:.1f} раз")
print(f"  ✓ binary быстрее line в {data['line'][-1]/data['binary'][-1]:.1f} раз")
print(f"  ✓ binary_fast быстрее binary в {data['binary'][-1]/data['binary_fast'][-1]:.1f} раз")
print(f"\n💡 Вывод:")
print(f"   При растущем M квадратичная сложность O(N·M) у line становится")
print(f"   критичной. Алгоритмы с O(N·log M) и O(N+M) выигрывают на больших данных.")
print("=" * 70)
print("\n✅ График сохранён как benchmark_with_growing_M.png")
