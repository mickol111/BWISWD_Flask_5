from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import datetime as dt
import pandas_datareader.data as web

pd.options.plotting.backend = "plotly"

start = dt.datetime(2013, 1, 1)
end = dt.datetime.today()
df_DJI = web.DataReader('^DJI', 'stooq', start=start, end=end)
df_DJI = df_DJI.drop(['Volume'], axis=1)
df_DAX = web.DataReader('^DAX', 'stooq', start=start, end=end)
df_DAX = df_DAX.drop(['Volume'], axis=1)
df_NDQ = web.DataReader('^NDQ', 'stooq', start=start, end=end)
df_NDQ = df_NDQ.drop(['Volume'], axis=1)


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

#fig = px.bar(df_DJI, y='Close', color='black', barmode="group")
fig = df_DJI['Close'].plot(title="Dow Jones Industries")
fig1 = df_DAX['Close'].plot(title="DAX")
fig2 = df_NDQ['Close'].plot(title="NASDAQ")

app.layout = html.Div(children=[
    html.H1(children='BWiSWD. Projekt 05'),

    html.Div(children='''
        Michał Kolankowski
    '''),

    dcc.Graph(
        id='fig',
        figure=fig
    ),
    dcc.Graph(
        id='fig1',
        figure=fig1
    ),
    dcc.Graph(
        id='fig2',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)