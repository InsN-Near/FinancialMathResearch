import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as ps # adicionado

np.random.seed(1) 
n = 8000
df = pd.DataFrame()
df['Date'] = pd.date_range(start='2022-02-25', periods=n, freq='D') 
df['Open'] = np.zeros(n) 
df['Close'] = np.zeros(n) 
df['Open'][0] = np.random.uniform(low=100, high=200) 
df['Close'][0] = df['Open'][0] + np.random.normal(scale=10) 
for i in range(1, n): 
    
    df.loc[i, 'Open'] = df.loc[i-1, 'Close'] 
    
    df.loc[i, 'Close'] = df.loc[i, 'Open'] + np.random.normal(scale=10) 
df['High'] = df[['Open', 'Close']].max(axis=1) + np.random.uniform(low=0, high=10, size=n) 
df['Low'] = df[['Open', 'Close']].min(axis=1) - np.random.uniform(low=0, high=10, size=n) 
df['Color'] = np.where(df['Close'] >= df['Open'], 'green', 'red') 

# calculando o MACD
periodo_rapido = 12 # período da média móvel rápida
periodo_lento = 26 # período da média móvel lenta
periodo_sinal = 9 # período da média móvel do sinal

ema_rapida = df['Close'].ewm(span=periodo_rapido, adjust=False).mean() # média móvel exponencial rápida
ema_lenta = df['Close'].ewm(span=periodo_lento, adjust=False).mean() # média móvel exponencial lenta
macd = ema_rapida - ema_lenta # diferença entre as médias móveis
sinal = macd.ewm(span=periodo_sinal, adjust=False).mean() # média móvel exponencial do MACD
histograma = macd - sinal # diferença entre o MACD e o sinal

# criando um subplot com duas linhas e uma coluna
fig = ps.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights= (3,1,), # adicionado
                       subplot_titles=['Gráfico de candlesticks aleatório PTFX', # adicionado
                                       'Gráfico de MACD']) # adicionado

# adicionando o gráfico de candlesticks na primeira linha
fig.add_trace(go.Candlestick(x=df['Date'], 
                open=df['Open'], 
                high=df['High'], 
                low=df['Low'], 
                close=df['Close'], 
                increasing_line_color= 'green', 
                decreasing_line_color= 'red'), row=1, col=1) # adicionado

# adicionando o gráfico de MACD na segunda linha
fig.add_trace(go.Scatter(x=df['Date'], 
                         y=macd, 
                         mode='lines', 
                         line=dict(color='blue'), 
                         name='MACD'), row=2, col=1) # adicionado
fig.add_trace(go.Scatter(x=df['Date'], 
                         y=sinal, 
                         mode='lines', 
                         line=dict(color='orange'), 
                         name='Sinal'), row=2, col=1) # adicionado
fig.add_trace(go.Bar(x=df['Date'], 
                     y=histograma, 
                     marker_color='gray', 
                     name='Histograma'), row=2, col=1) # adicionado

# atualizando o layout do gráfico
fig.update_layout(title='Gráficos interativos com Plotly', 
                  xaxis_title='Data', 
                  yaxis_title='Preço', 
                  yaxis2_title='MACD', # adicionado
                  showlegend=True,
                  plot_bgcolor='black',
                  yaxis=dict(autorange=True, 
                             fixedrange=False)) 
fig.update_layout(xaxis={'rangeslider': {'visible': False}})

fig.show()
