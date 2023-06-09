import plotly.graph_objs as go
import plotly.offline as pyo
import sqlite3 as sq

conn = sq.connect('csgopoly.db')
cur = conn.cursor()

def createGraphics():
    cur.execute("SELECT coeff FROM casino_hack")
    coeff = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT time FROM casino_hack")
    time = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT deposit FROM casino_hack")
    deposit = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT profit FROM casino_hack")
    profit = [row[0] for row in cur.fetchall()]


    trace = go.Scatter(x=time, y=coeff)
    layout = go.Layout(title='Простой график', xaxis=dict(title='ВРЕМЯ'), yaxis=dict(title='ДЕНЬГИ'))

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_layout(
        yaxis=dict(
            dtick=1
        )
    )
    pyo.plot(fig, filename='simple_plot.html')

createGraphics()