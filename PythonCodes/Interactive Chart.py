import numpy as np
import pandas as pd
import plotly.graph_objects as go

np.random.seed(1) 
n = 800
df = pd.DataFrame()
df['Date'] = pd.date_range(start='2023-02-25', periods=n, freq='D') 
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

fig = go.Figure(data=[go.Candlestick(x=df['Date'], 
                open=df['Open'], 
                high=df['High'], 
                low=df['Low'], 
                close=df['Close'], 
                increasing_line_color= 'green', 
                decreasing_line_color= 'red')]) 

fig.update_layout(title='Gráfico de candlesticks aleatório PTFX', 
                  xaxis_title='Data', 
                  yaxis_title='Preço', 
                  showlegend=True,
                  plot_bgcolor='black',
                  yaxis=dict(autorange=True, 
                             fixedrange=False)) 

#fig.update_layout(xaxis={'rangeslider': {'visible': False}})

fig.show()
