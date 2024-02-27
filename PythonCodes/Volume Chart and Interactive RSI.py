import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as ps
import time

def media_movel(dados, janela):
    media_movel_lista = []
    for i in range(len(dados) - janela + 1):
        media_movel = sum(dados[i:i+janela])/janela
        media_movel_lista.append(media_movel)
    return media_movel_lista

np.random.seed(int(time.time()))
n = 6000
df = pd.DataFrame()
df['Date'] = pd.date_range(start='2010-10-01', periods=n, freq='D')
df['Open'] = np.zeros(n)
df['Close'] = np.zeros(n)
df.loc[0, 'Open'] = np.random.uniform(low=100, high=200)
df.loc[0, 'Close'] = df.loc[0, 'Open'] + np.random.normal(scale=10)
for i in range(1, n):
    df.loc[i, 'Open'] = df.loc[i-1, 'Close']
    df.loc[i, 'Close'] = df.loc[i, 'Open'] + np.random.normal(scale=10)
df['High'] = df[['Open', 'Close']].max(axis=1) + np.random.uniform(low=0, high=10, size=n)
df['Low'] = df[['Open', 'Close']].min(axis=1) - np.random.uniform(low=0, high=10, size=n)
df['Color'] = np.where(df['Close'] >= df['Open'], 'green', 'red')

media_movel_20 = media_movel(df['Close'], 20)
media_movel_50 = media_movel(df['Close'], 50)
media_movel_200 = media_movel(df['Close'], 200)

df['Volume Indexado'] = (df['High'] - df['Low']) * 10

df['Variação'] = df['Close'].diff()

df['Variação Positiva'] = np.where(df['Variação'] > 0, df['Variação'], 0)
df['Variação Negativa'] = np.abs(np.where(df['Variação'] < 0, df['Variação'], 0))

timeperiod = 9 
df['Média Exponencial Positiva'] = df['Variação Positiva'].ewm(alpha=1/timeperiod).mean()
df['Média Exponencial Negativa'] = df['Variação Negativa'].ewm(alpha=1/timeperiod).mean()

df['RSI'] = 100 - (100 / (1 + (df['Média Exponencial Positiva'] / df['Média Exponencial Negativa'])))

rsi = df['RSI']

fig = ps.make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.02, row_heights= [3,1,1],
                       subplot_titles=['Gráfico de candlesticks aleatório com médias móveis e bandas de bollinger',
                                       'Gráfico de volume indexado',
                                       'Gráfico de RSI'])

fig.add_trace(go.Candlestick(x=df['Date'],
                             open=df['Open'],
                             high=df['High'],
                             low=df['Low'],
                             close=df['Close'],
                             increasing_line_color= 'green',
                             decreasing_line_color= 'red',
                             name='Candlesticks'), row=1, col=1)

fig.add_trace(go.Scatter(x=df['Date'][19:],
                         y=media_movel_20,
                         mode='lines',
                         line=dict(color='blue'),
                         name='Média Móvel de 20 dias'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Date'][49:],
                         y=media_movel_50,
                         mode='lines',
                         line=dict(color='orange'),
                         name='Média Móvel de 50 dias'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Date'][199:],
                         y=media_movel_200,
                         mode='lines',
                         line=dict(color='purple'),
                         name='Média Móvel de 200 dias'), row=1, col=1)

fig.add_trace(go.Bar(x=df['Date'],
                     y=df['Volume Indexado'],
                     marker_color='gray',
                     name='Volume Indexado'), row=2, col=1)

fig.add_trace(go.Scatter(x=df['Date'],
                         y=rsi,
                         mode='lines',
                         line=dict(color='white'),
                         name='RSI'), row=3, col=1)
fig.add_trace(go.Scatter(x=df['Date'],
                         y=np.full(n, 30),
                         mode='lines',
                         line=dict(color='red', dash='dash'),
                         name='Limite Inferior'), row=3, col=1)
fig.add_trace(go.Scatter(x=df['Date'],
                         y=np.full(n, 70),
                         mode='lines',
                         line=dict(color='green', dash='dash'),
                         name='Limite Superior'), row=3, col=1)

fig.update_layout(title='Gráficos interativos com Plotly',
                  xaxis_title='Data',
                  yaxis_title='Preço',
                  yaxis2_title='Volume Indexado',
                  yaxis3_title='RSI',
                  showlegend=True,
                  plot_bgcolor='black')

fig.update_yaxes(fixedrange=False)

fig.update_layout(xaxis={'rangeslider': {'visible': False}})

fig.show()
