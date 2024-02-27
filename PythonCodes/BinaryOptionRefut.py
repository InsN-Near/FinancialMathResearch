
import numpy as np
import matplotlib.pyplot as plt


valor_investido = 100 
taxa_acerto = 0.55 
retorno = 0.8
operacoes_dia = 10 
dias_mes = 20 
operacoes_mes = operacoes_dia * dias_mes


resultados = []

saldo = 0


for i in range(operacoes_mes):
 
  aleatorio = np.random.rand()
 
  if aleatorio < taxa_acerto:
   
    saldo = saldo + valor_investido * retorno
    
    resultados.append(saldo)

  else:
   
    saldo = saldo - valor_investido
   
    resultados.append(saldo)

plt.plot(resultados, color='green')
plt.xlabel('Número de operações')
plt.ylabel('Saldo (R$)')
plt.title('Simulação de opções binárias')
plt.show()
