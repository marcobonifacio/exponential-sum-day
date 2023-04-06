import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

d = dt.datetime.today().day
m = dt.datetime.today().month
y = dt.datetime.today().year

def f(n, d, m, t):
    return n / d + n ** 2 / m + n ** 3 / y

def p(giorno, mese, anno, N, step):
    z = np.array([np.exp(2 * np.pi * 1j * f(n, giorno, mese, anno)) for n in range(3, N * 3, step)])
    z = z.cumsum()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(z.real, z.imag, color='#4c78a8')
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'{giorno:02d}-{mese:02d}-{anno}')
    return fig

display(p(d, m, y, 10000, 1))
