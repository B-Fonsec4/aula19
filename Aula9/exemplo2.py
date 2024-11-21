import pandas as pd 
import numpy as np 
dados = pd.Series([2,4,6,8,10])
#transformando os dados em array numpy
conjunto_dados = np.array(dados)
media = conjunto_dados.mean()
variancia = np.var(conjunto_dados)
desvio = np.std(conjunto_dados)


print(f'conjuntos de dados: {conjunto_dados}')
print(f'Média: {conjunto_dados.mean()}')
#calcula a variancia
print(f'A Variancia da serie de dados: {np.var(conjunto_dados)}')
# calcula o desvio padrão
print(f'Desvio padrão da serie de dados: {np.std(conjunto_dados):.2f}')

distancia_var_media = variancia / (media **2)
print(f'Distancia entre Variancia e media: {distancia_var_media:.2f}')
coef_variacao = (desvio / media)*100
print(f'Coeficiente de variação: {coef_variacao:.2f}')
