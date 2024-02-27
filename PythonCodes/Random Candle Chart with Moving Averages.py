import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Gráfico de candlesticks aleatório com médias móveis')
ax.set_xlabel('Data')
ax.set_ylabel('Preço')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
ax.grid(True)
for i in range(n):
    ax.vlines(x=df['Date'][i], ymin=df['Open'][i], ymax=df['Close'][i], color=df['Color'][i], linewidth=6)
    ax.vlines(x=df['Date'][i], ymin=df['Low'][i], ymax=df['High'][i], color=df['Color'][i])
ax2 = ax.twinx()
ax2.plot(df['Date'][19:], media_movel_20, color='blue', label='Média Móvel de 20 dias')
ax2.plot(df['Date'][49:], media_movel_50, color='orange', label='Média Móvel de 50 dias')
ax2.plot(df['Date'][199:], media_movel_200, color='purple', label='Média Móvel de 200 dias') 
ax.yaxis.label.set_color('red')
ax2.yaxis.label.set_color('blue')
ax.legend(loc='upper left', bbox_to_anchor=(0, 1), frameon=False)
ax2.legend(loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
ax.set_xlim(df['Date'][n-80], df['Date'].iloc[-1])
plt.show()