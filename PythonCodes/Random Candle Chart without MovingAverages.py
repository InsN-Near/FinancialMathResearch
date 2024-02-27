#Este código gera, a partir da seed, um gráfico de Velas automático. De autoria do Grande Mestre Paulo Texugo.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Não precisa de comentários
#mas se quiser um gráfico aleatório dá um "import time" e coloca aqui embaixo um "np.random.seed(int(time.time()))"
np.random.seed(0) 
n = 80 
df = pd.DataFrame()
df['Date'] = pd.date_range(start='2023-02-25', periods=n, freq='D') 
df['Open'] = np.zeros(n) 
df['Close'] = np.zeros(n) 
df['Open'][0] = np.random.uniform(low=100, high=200) 
df['Close'][0] = df['Open'][0] + np.random.normal(scale=10) 
for i in range(1, n): #essa foi a minha solução genial kkkkkk
    
    df.loc[i, 'Open'] = df.loc[i-1, 'Close'] #Aí o reço de abertura é igual ao preço de fechamento da vela anterior
    
    df.loc[i, 'Close'] = df.loc[i, 'Open'] + np.random.normal(scale=10) #adicionar valor aleatório, o que eu te falei. E a definiçao de limites
df['High'] = df[['Open', 'Close']].max(axis=1) + np.random.uniform(low=0, high=10, size=n) 
df['Low'] = df[['Open', 'Close']].min(axis=1) - np.random.uniform(low=0, high=10, size=n) 
df['Color'] = np.where(df['Close'] >= df['Open'], 'green', 'red') 

#aqui tu vai rachar kkkkkkkkkkkkkkk, a genialidade dos candles
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Gráfico de candlesticks aleatório PTFX')
ax.set_xlabel('Data')
ax.set_ylabel('Preço')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
ax.grid(True) 
for i in range(n): 
    #kkkkkkkkkkkkkkkkkkkk namoral, pô, não zoa, ficou muito bom 
    ax.vlines(x=df['Date'][i], ymin=df['Open'][i], ymax=df['Close'][i], color=df['Color'][i], linewidth=6)
    ax.vlines(x=df['Date'][i], ymin=df['Low'][i], ymax=df['High'][i], color=df['Color'][i])
plt.show()