import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

import js

in_date = js.document.getElementById('in-date')
in_n = js.document.getElementById('in-N')
in_step = js.document.getElementById('in-step')
spin = js.document.getElementById('spin')

in_date.value = dt.datetime.today().strftime('%Y-%m-%d')

def f(n, d, m, y):
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
    spin.style.visibility = 'visible'
    try:
      y, m, d = [int(n) for n in in_date.value.split('-')]
    except ValueError:
      y, m, d = [int(n) for n in dt.datetime.today().strftime('%Y-%m-%d').split('-')]
    n = int(in_n.value) * 10000
    step = int(in_step.value)
    display(n, target='out-N', append=False)
    display(step, target='out-step', append=False)
    display(f'{d:02d}-{m:02d}-{y}', target='date', append=False)
    display(p(d, m, y, n, step), target='canvas', append=False)
    spin.style.visibility = 'hidden'

update()
