import pandas as pd 
import numpy as np
idades = pd.Series([5,10,12,35,38])
todas_idade = np.array(idades)
media = todas_idade.mean()
variancia_amostral = np.var(todas_idade, ddof=1)
desvio_amostral= np.std(todas_idade,ddof=1)
print(f'Media: {media} ')
print(f'A variancia das idades é: {variancia_amostral:.2f}')
print(f'Desvio padrão de dados é: {desvio_amostral:.2f}')

# distancia_var_media = variancia / (media**2)
# print(f'A distancia entre a variancia e a media: {distancia_var_media:.2f}')

# coef_variacao = (desvio / media) *100
# print(f'Coeficiente de variação: {coef_variacao:.2f}')