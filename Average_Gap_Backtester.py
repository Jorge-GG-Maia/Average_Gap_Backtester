import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from PIL import Image

tipo = int(input('Qual tipo de operação deseja simular? [1: Compra e venda, 2: Somente compra, 3: Somente venda]''\n'))

#Função que avalia a formação das posições de Long & Short baseada na relação à distancia entre médias e os dois desvios padrões
#... a mais e a menos da própria média
def LongShort(dados, tipo):
	Valor = dados['Distancia']
	BandaMax = dados['Banda+']
	BandaMin = dados['Banda-']
	Media = dados['Media']

	LongShort = []
	LongShort.append(0)

	for i in range(1, len(Valor)):

		if Valor[i-1] >= BandaMax[i-1]:
			LongShort.append(-1) if tipo != 2 else LongShort.append(0)

		elif Valor[i-1] <= BandaMin[i-1]:
			LongShort.append(1) if tipo != 3 else LongShort.append(0)

		elif Valor[i-1] == 0:
			LongShort.append(0)

		else:
			LongShort.append(LongShort[-1])


	LongShort = np.array(LongShort)

	return LongShort

#Função que calcula e gera o Data Frame com os dados e variáveis que serão usadas
def NDF(dados, ativo):

	NDF = pd.DataFrame()

	Valores = dados['Fechamento']

	Var = []
	Var.append(0)

	for i in range(1, len(Valores)):

		Var.append((Valores[i] - Valores[i-1]) / Valores[i-1])

	Var = np.array(Var)


	NDF['Data'] = dados['Data']
	NDF['Fechamento'] = dados['Fechamento']
	NDF['Var%'] = Var

	NDF['MM5'] = dados['Fechamento'].rolling(window = 5).mean()
	NDF['MM20'] = dados['Fechamento'].rolling(window = 20).mean()


	NDF['Distancia'] = NDF['MM5'] - NDF['MM20']
	NDF['Desvio'] = NDF['Distancia'].rolling(window = 20).std()
	NDF['Media'] = NDF['Distancia'].rolling(window = 20).mean()

	NDF['Banda+'] = NDF['Media'] + (2 * NDF['Desvio'])
	NDF['Banda-'] = NDF['Media'] - (2 * NDF['Desvio'])

	NDF = NDF[40:len(NDF)]
	NDF.to_csv(str(ativo + ' - DadosProcessados.csv'), index = False)
	Final = pd.read_csv(str(ativo + ' - DadosProcessados.csv'))	

	return Final


#Função que calcula os retornos acumulados baseado nas posições de compra e venda em comparação aos retornos do Buy and Hold 
def BackTest(dados, ativo):

	var = dados['Var%']
	longshort = dados['LongShort']

	retornos = var * longshort

	acumulado = []
	acumulado.append(1000)
	bh = []
	bh.append(1000)

	intervalo = []
	intervalo.append(0)

	for i in range(1, len(retornos)):
		acumulado.append(acumulado[-1] * (1 + retornos[i]))
		bh.append(bh[i-1] * (1 + var[i]))
		intervalo.append(intervalo[-1] + 1)

	acumulado = np.array(acumulado)
	bh = np.array(bh)

	Backtest = pd.DataFrame()
	Backtest['Data'] = dados['Data']
	Backtest['Var%'] = var
	Backtest['Retornos'] = retornos
	Backtest['Modelo'] = acumulado
	Backtest['Buy&Hold'] = bh

	plt.plot(intervalo, acumulado, intervalo, bh)
	plt.legend([str('Modelo: ' + ativo), 'Buy&Hold'])
	plt.savefig(str(ativo + '.png'))

	Backtest.to_csv(str(ativo + ' - Retornos.csv'), index = False)
	return Backtest

#Faz a leitura de todoas as bases de dados presentes na pasta e executa o processamento dos dados e simulação das operações
lista = os.listdir('/home/jorge/Documentos/Average_Gap_Backtester/Database/')
ativos = []
codigos = []

for nome in lista:
	if nome.endswith('.csv') == True:
		codigo = os.path.splitext(nome)[0]
		ativos.append(codigo)
		codigos.append(nome)


for ativo in ativos:

	dados = pd.read_csv(str('/home/jorge/Documentos/Average_Gap_Backtester/Database/' + ativo + '.csv'))

	ndf = NDF(dados, ativo)

	ndf['LongShort'] = LongShort(ndf, tipo)
	bk = BackTest(ndf, ativo)

	#print(bk)

	retornos = np.array(bk['Modelo'])
	benchmark = np.array(bk['Buy&Hold'])

	VarModelo = ((retornos[-1] - retornos[0] ) / retornos[0] ) * 100
	VarBH = ((benchmark[-1] - benchmark[0]) / benchmark[0]) * 100

	VarModelo = round(VarModelo,2)
	VarBH = round(VarBH,2)

	print(ativo, ' - Acumulado: ', VarModelo, '%', ' Buy&Hold: ', VarBH, '%')
	plt.show()

