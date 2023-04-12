import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

import js

today = dt.datetime.today()

d = today.day
m = today.month
y = today.year

div_date = js.document.getElementById('div-date')
in_date = js.document.getElementById('in-date')
in_n = js.document.getElementById('in-N')
in_step = js.document.getElementById('in-step')

in_date.value = today.strftime('%Y-%m-%d')

def f(n, d, m, t):
    return n / d + n ** 2 / m + n ** 3 / y

def p(giorno, mese, anno, N, step):
    z = np.array([np.exp(2 * np.pi * 1j * f(n, giorno, mese, anno)) 
        for n in range(3, N * 3, step)])
    z = z.cumsum()
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(z.real, z.imag, color='#4682b4')
    ax.set_aspect(1)
    plt.axis('off')
    return fig

def update(): 
    y, m, d = [int(n) for n in in_date.value.split("-")]
    n = int(in_n.value) * 10000
    step = int(in_step.value)
    div_date.innerHTML = f'{d:02d}-{m:02d}-{y}'
    display(p(d, m, y, n, step), target='canvas')

update()
