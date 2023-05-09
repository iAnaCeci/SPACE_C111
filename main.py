import numpy as np

arr = np.loadtxt('space.csv',
                 delimiter=';',
                 encoding='utf-8',
                 dtype=str)

#Questao1
# print(len(arr[1:,7])-np.count_nonzero(np.char.find(arr[1:,7],('Success'))))
# sucessos = len(arr[1:, 7]) - np.count_nonzero(np.char.find(arr[1:, 7], "Success"))
# print(((sucessos/len(arr[1:, 7]))*100)) #Porcentagem

#Questao2
#
# num_missoes=np.max(arr[1:,0].astype('int'))
# total_gasto=np.sum(arr[1:,6].astype('float'))
# print(f'N de missões: {num_missoes}')
# print(f'Total gasto: {total_gasto}')
# print(f'Média: {(total_gasto/num_missoes)} ')

#Questao3

# pais=arr[1:,2] #[1:significa= a partir da linha 1, e o 2 significa a coluno]
# EUA=np.char.endswith(pais,"USA")
# num_USA=np.sum(EUA)
# print(f'Realizadas {num_USA} missões')

#Questao4
# spaceX=(arr[1:,(1,6)]) # a partir da linha 1, vou pegar oq ta na coluna 1 e 6
# custos=arr[1:,6]
# maior_valor=np.max(custos[(spaceX[0:,0]=="SpaceX")].astype('float32'))
# print(f'A missão de maior custo foi {maior_valor} milhões')

#Questão 5

# companhias = np.unique(arr[1:, 1])
#
# for empresa in companhias:
#     aux = np.char.find(arr[1:, 1], empresa)
#     num_missoes = np.sum(aux>=0)
#     print(f'Compania: {empresa}\nTotal: {num_missoes}')
