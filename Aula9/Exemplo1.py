dados = {1,2,3,4,5}
media = sum(dados)/len(dados)
print(f'Media: {media}')
# calcular media dos quadados da diferença
diferencas = [x - media for x in dados]
print(f'Diferença em relação a media: {diferencas}')
# elevar diferença ao quadrado
quadrado_diferenca = [x**2 for x in diferencas]
print(f'Quadrado das diferenças: {quadrado_diferenca}')
# calcular a media dos quadrados das diferenças
media_quadrado_diferenca = sum(quadrado_diferenca)/ len(quadrado_diferenca)
print(f'VAriancia é a media dos quadrados das diferenças: {media_quadrado_diferenca}')
#calcular a raiz quadrada da media dos quadrados das diferenças
desvio_padrao = media_quadrado_diferenca **0.5
print(f'Desvio padrão é a raiz quadrada da variância: {desvio_padrao}')