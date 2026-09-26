import matplotlib.pyplot as plt
import numpy as np

data = {
    'bytes': [1357, 2755, 5625, 10983, 21793, 43421, 87519, 175405],
    'line': [0.000012, 0.000031, 0.000088, 0.000171, 0.000320, 0.000569, 0.001200, 0.002432],
    'binary': [0.000037, 0.000090, 0.000172, 0.000319, 0.000581, 0.001102, 0.002195, 0.004525],
    'hash_set': [0.000008, 0.000016, 0.000027, 0.000052, 0.000095, 0.000176, 0.000389, 0.000827],
    'binary_fast': [0.000032, 0.000066, 0.000140, 0.000263, 0.000490, 0.000938, 0.001932, 0.004058]
}

plt.figure(figsize=(10, 6))
plt.plot(data['bytes'], data['line'], marker='o', label='line')
plt.plot(data['bytes'], data['binary'], marker='s', label='binary')
plt.plot(data['bytes'], data['hash_set'], marker='^', label='hash_set')
plt.plot(data['bytes'], data['binary_fast'], marker='d', label='binary_fast')

plt.xlabel('Размер в байтах')
plt.ylabel('Время (секунды)')
plt.title('Зависимость времени выполнения от размера данных')
plt.legend()
plt.grid(True)
plt.xscale('log')  # Логарифмическая шкала для X
plt.yscale('log')  # Логарифмическая шкала для Y (опционально)
plt.show()
