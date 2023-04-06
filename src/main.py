import datetime as dt
import numpy as np
import pandas as pd
import altair as alt

d = dt.datetime.today().day
m = dt.datetime.today().month
y = dt.datetime.today().year

def f(n, d, m, t):
    return n / d + n ** 2 / m + n ** 3 / y

def p(giorno, mese, anno, N, step):
    z = np.array([np.exp(2 * np.pi * 1j * f(n, giorno, mese, anno)) for n in range(3, N * 3, step)])
    z = z.cumsum()
    df = pd.DataFrame([z.real, z.imag]).T.reset_index()
    df.columns = ['sort', 'real', 'imag']
    alt.data_transformers.enable('json')
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X('real', axis=alt.Axis(title='')),
        y=alt.Y('imag', axis=alt.Axis(title='')),
        order='sort'
    ).properties(
        title='{}/{}/{}'.format(giorno, mese, anno)
    ).configure(
        title=alt.VgTitleConfig(font='calibri', fontSize=16, fontWeight='bold')
    ).configure_axis(
        grid=False, 
        domain=False, 
        labels=False, 
        ticks=False,
    ).configure_view(
        strokeOpacity=0,
        height=350,
        width=350
    )
    return chart

display(p(d, m, y, 10000, 1))
