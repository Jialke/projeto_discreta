'''Aluno: Lucas da Costa Paula

O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: 
-a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; 
-as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código
da operação (U para união, I para interseção, D para diferença e C produto cartesiano), 
a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas.
'''

# Váriavel para armazenar as operações de forma separada dentro do código
operacoes = []

# Leitura de arquivo de entradas, deve-se trocar a numeração do arquivo (arquivo1.txt até arquivo4.txt) para trocar as entradas
with open('entradas4.txt', 'r') as arquivo:
    entradas = arquivo.readlines()

# Quantidade de operações para definir execução do programa
qtd = int(entradas[0]) # Coleta de quantidade de operações da lista de entradas
del(entradas[0]) # Deletar a primeira linha para coletar as demais informações da lista posteriormente

# Coleta de dados: Código de operação e os conjuntos separados em uma matriz de n x 3 [operação, conjunto1, conjunto2]
for i in range(qtd):
    entrada = entradas[:3] # Coleta as 3 primeiras linhas da lista de entradas
    operacoes.append(entrada) # Coloca as linhas coletadas dentro de uma unica linha na lista operações
    del(entradas[:3]) # Deleta as 3 linhas coletadas para continuar o loop

# Realização de operações de conjuntos
for j in range(qtd):
    operacao = operacoes[j][0]
    conjunto1 = set(operacoes[j][1].strip().split(', ')) #transformar em set para operações de conjuntos e split e strip usados para deletar os espaços vazios entre os valores
    conjunto2 = set(operacoes[j][2].strip().split(', '))

    match operacao:
        case 'U\n':
            result = conjunto1.union(conjunto2) #União
            print('União: conjunto 1', conjunto1,', conjunto 2', conjunto2,'. Resultado:', result)
        case 'I\n':
            result = conjunto1.intersection(conjunto2) #Intersecção
            print('Intersecção: conjunto 1', conjunto1,', conjunto 2', conjunto2,'. Resultado:', result)
        case 'D\n':
            result = conjunto1.difference(conjunto2) #Diferença
            print('Diferença: conjunto 1', conjunto1,', conjunto 2', conjunto2,'. Resultado:', result)
        case 'C\n':
            result = conjunto1.symmetric_difference(conjunto2) #Diferença Simétrica
            print('Diferença simétrica: conjunto 1', conjunto1,', conjunto 2', conjunto2,'. Resultado:', result)