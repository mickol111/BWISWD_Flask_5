from flask import Flask, render_template,request
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import json
import plotly
import plotly.express as px

#pd.options.plotting.backend = "plotly"

start = dt.datetime(2013, 1, 1)
end = dt.datetime.today()
df_DJI = web.DataReader('^DJI', 'stooq', start=start, end=end)
df_DJI = df_DJI.drop(['Volume'], axis=1)
df_DJI.index = df_DJI.index.strftime('%Y-%m-%d')
df_DAX = web.DataReader('^DAX', 'stooq', start=start, end=end)
df_DAX = df_DAX.drop(['Volume'], axis=1)
df_NDQ = web.DataReader('^NDQ', 'stooq', start=start, end=end)
df_NDQ = df_NDQ.drop(['Volume'], axis=1)

print(df_DJI.describe())
print(df_DJI.describe().to_html())

app = Flask(__name__)


@app.route("/")
def main():
    result = df_DJI.to_json(orient="split")
    posty1 = json.loads(result)
    table1 = df_DJI.describe().to_html()
    table2 = df_DAX.describe().to_html()
    table3 = df_NDQ.describe().to_html()

    df = pd.DataFrame({
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                  'Bananas'],
        'Amount': [4, 1, 2, 2, 4, 5],
        'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })
    fig = px.bar(df, x='Fruit', y='Amount', color='City',
                 barmode='group')
    #fig = df_DJI['Close'].plot(title="Dow Jones Industries")
    #fig1 = df_DAX['Close'].plot(title="DAX")
    #fig2 = df_NDQ['Close'].plot(title="NASDAQ")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    #graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    #graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', tytul1='Dow Jones Industries', tytul2='DAX',tytul3='NASDAQ', table1=table1,
                           table2=table2, table3=table3, graphJSON=graphJSON)#, graphJSON1=graphJSON1, graphJSON2=graphJSON2)

if __name__ == "__main__":
    app.run()
