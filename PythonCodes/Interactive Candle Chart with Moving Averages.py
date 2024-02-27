import numpy as np
import pandas as pd
import plotly.graph_objects as go 
import time

def media_movel(dados, janela):
    media_movel_lista = []
    for i in range(len(dados) - janela + 1):
        media_movel = sum(dados[i:i+janela])/janela
        media_movel_lista.append(media_movel)
    return media_movel_lista

np.random.seed(int(time.time()))
n = 500 
df = pd.DataFrame()
df['Date'] = pd.date_range(start='2021-10-01', periods=n, freq='D')
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

fig = go.Figure(data=[go.Candlestick(x=df['Date'], 
                open=df['Open'], 
                high=df['High'], 
                low=df['Low'], 
                close=df['Close'], 
                increasing_line_color= 'green', 
                decreasing_line_color= 'red')]) 

fig.update_layout(title='Gráfico de candlesticks aleatório com médias móveis', 
                  xaxis_title='Data', 
                  yaxis_title='Preço', 
                  yaxis=dict(autorange=True, 
                             fixedrange=False)) 


fig.add_trace(go.Scatter(x=df['Date'][19:], 
                         y=media_movel_20,
                         mode='lines',
                         line=dict(color='blue'),
                         name='Média Móvel de 20 dias'))
fig.add_trace(go.Scatter(x=df['Date'][49:], 
                         y=media_movel_50,
                         mode='lines',
                         line=dict(color='orange'),
                         name='Média Móvel de 50 dias'))
fig.add_trace(go.Scatter(x=df['Date'][199:], 
                         y=media_movel_200,
                         mode='lines',
                         line=dict(color='purple'),
                         name='Média Móvel de 200 dias'))

#fig.update_layout(xaxis={'rangeslider': {'visible': False}})

fig.show() 
