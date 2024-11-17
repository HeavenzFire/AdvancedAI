import numpy as np

phi = (1 + 5**0.5) / 2
fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

hub = np.array([phi, phi, phi, phi, phi])

print("Golden Ratio:", phi)
print("Fibonacci Sequence:", fib_sequence)
print("Flower of Life Hub:", hub)
