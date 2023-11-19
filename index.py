import time
import pandas as pd
import math



# essa função eu criei para transforma os minutos deciamis em Hora para facilitar meu entendimento durante o codigo e validar as informações 
def minutos_para_hora(minutos_decimais):
    horas = int(minutos_decimais // 60)
    minutos = int(minutos_decimais % 60)
    return time.strftime("%H:%M", time.strptime(f"{horas}:{minutos}", "%H:%M"))


x = 0
y = 0
# primeiro passo é ler o arquivo e saber quantas linhas ele tem, ate porque caso eu queira adicionar outros valores o programa tem que funcionar *-*
banco =  pd.read_csv('airlines_delay.csv')

numero_de_linhas = banco.shape[0]


# calculando a entropia principal com base no atraso e não atraso, sendo x atraso e y não atraso
#explicando melhor o que esse for faz nada mais que é ler o arquivo e ver quantas vezes ele atrasou e não atrasou para realizar o calculo da entropia
for teste in banco['Class']:
    if teste == 1:
        x = x + 1
    else:
        y = y + 1


positivo = y/numero_de_linhas

negativo = x/numero_de_linhas


entropia = (-positivo * math.log2(positivo) - negativo * math.log2(negativo))

#agora temos a entropia principal agora vamo verificar a entropia das classes começando por companhia, eu pra achar as companhia que é representada eu filtrei atras do pandas apenas as companhia e to tratando elas abaixos, vou deixar a maneira como eu fiz no arquivo teste.py

# começando a tratar as classes começando pela  Airline que é a companhia 
DL = 0
OO = 0
B6 = 0
US = 0
FL = 0 
WN = 0
CO = 0
AA = 0
YV = 0 
EV = 0 
XE = 0
_9E= 0
OH = 0
UA = 0 
MQ = 0 
AS = 0 
F9 = 0
HA = 0
#o nunique vai ver todas as linhas e vai pegar as companias apenas uma vez mesmo que ela apareça varias vezes, isso é necessario para eu fazer o calculo do ganho da classe
companias = banco['Airline']
# companhias para anotação DL OO B6 US FL WN CO AA YV EV XE 9E OH UA MQ AS F9 HA
for cont in companias: 
    if cont == 'DL': 
        DL = DL + 1
    elif cont == 'OO':
        OO = OO + 1
    elif cont == 'B6':
       B6 = B6 + 1 
    elif cont == 'US':
        US = US + 1
    elif cont == 'FL':
        FL = FL + 1
    elif cont == 'WN':
        WN = WN + 1
    elif cont == 'CO':
        CO = CO + 1 
    elif cont == 'AA':
        AA = AA + 1
    elif cont == 'YV':
        YV = YV + 1
    elif cont == 'EV':   
        EV = EV + 1
    elif cont == 'XE':
        XE = XE + 1
    elif cont == '9E':
        _9E = _9E + 1
    elif cont == 'OH':
        OH = OH + 1
    elif cont == 'UA':
        UA = UA + 1
    elif cont == 'MQ':
        MQ = MQ + 1
    elif cont == 'AS':
        AS = AS + 1
    elif cont == 'F9':
        F9 = F9 + 1
    else:
        HA = HA + 1
# QUANTIDADE DE VEZES EM CADA COMPANHIA 
#print(DL, OO, B6, US, FL, WN, CO, AA, YV, EV, XE, _9E, OH, UA, MQ, AS, F9, HA)

#agora a parti que tem que presta atenção pra não se perde, vamos filtrar quantas vezes cada companhia atrasou ou não 
#releve meus nomes de variaveis grandes xD

classe_atraso = 1
classe_tudook = 0

#jogar as companhias em uma variavel str Detalho caso os novos dados que vão inserir depois tenha companhias ineditas tera que ajustar essa parte e a anterios para tratar as novas companhias :)

sDL = 'DL'
sOO = 'OO'
sB6 = 'B6'
sUS = 'US'
sFL = 'FL'
sWN = 'WN'
sCO = 'CO'
sAA = 'AA'
sYV = 'YV'
sEV = 'YV'
sXE = 'XE'
s_9E= '9E'
sOH = 'OH'
sUA = 'UA'
sMQ = 'UA'
sAS = 'MQ'
sF9 = 'AS'
sHA = 'F9'

# agora vamos começar a filtar o filtro é o que recebe os dados atrasados e o 2 recebe sem atraso 

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sDL)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sDL)

dl_S = banco[filtro].shape[0]
dl_N = banco[filtro2].shape[0]
# A parti dai é só ler  a quantidade de casos de cada um e adicionar em variaveis. 
print(dl_N,dl_S)
print(dl_N+dl_S)
print(DL)