from main import Move
import matplotlib.pyplot as plt
import numpy as np


Fs = 2000
f = 5
sample = 80
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x * 10 / Fs) * 6

for a in y:
    b = Move(True, a, 0)
    b.move_win()
