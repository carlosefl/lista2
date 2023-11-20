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
sEV = 'EV'
sXE = 'XE'
s_9E= '9E'
sOH = 'OH'
sUA = 'UA'
sMQ = 'MQ'
sAS = 'AS'
sF9 = 'F9'
sHA = 'HA'

# agora vamos começar a filtar o filtro é o que recebe os dados atrasados e o 2 recebe sem atraso 

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sDL)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sDL)

dl_S = banco[filtro].shape[0]
dl_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sOO)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sOO)

OO_S = banco[filtro].shape[0]
OO_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sB6)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sB6)


B6_S = banco[filtro].shape[0]
B6_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sUS)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sUS)

US_S = banco[filtro].shape[0]
US_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sFL)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sFL)


FL_S = banco[filtro].shape[0]
FL_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sWN)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sWN)


WN_S = banco[filtro].shape[0]
WN_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sCO)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sCO)

CO_S = banco[filtro].shape[0]
CO_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sAA)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sAA)


AA_S = banco[filtro].shape[0]
AA_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sYV)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sYV)


YV_S = banco[filtro].shape[0]
YV_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sEV)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sEV)


EV_S = banco[filtro].shape[0]
EV_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sXE)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sXE)


XE_S = banco[filtro].shape[0]
XE_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == s_9E)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == s_9E)


_9E_S = banco[filtro].shape[0]
_9E_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sOH)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sOH)


OH_S = banco[filtro].shape[0]
OH_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sUA)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sUA)


UA_S = banco[filtro].shape[0]
UA_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sMQ)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sMQ)


MQ_S = banco[filtro].shape[0]
MQ_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sAS)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sAS)


AS_S = banco[filtro].shape[0]
AS_N = banco[filtro2].shape[0]

filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sF9)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sF9)


F9_S = banco[filtro].shape[0]
F9_N = banco[filtro2].shape[0]


filtro = (banco['Class'] == classe_atraso) & (banco['Airline'] == sHA)
filtro2 = (banco['Class'] == classe_tudook) & (banco['Airline'] == sHA)

HA_S = banco[filtro].shape[0]
HA_N = banco[filtro2].shape[0]
# A parti dai é só ler  a quantidade de casos de cada um e adicionar em variaveis. e vazer as conta pra ver se tem uma execeção muito grande, caso não tenha ai faz as contas da pureza da classe 

#print(dl_N,dl_S)
#print(OO_N,OO_S)
#print(B6_N, B6_S)
#print(US_N, US_S)
#print(FL_N,FL_S)
#print(WN_N,WN_S)
#print(CO_N,CO_S)
#print(AA_N,AA_S)
#print(YV_N,YV_S)
#print(EV_N,EV_S)
#print(XE_N,XE_S)
#print(_9E_N,_9E_S)
#print(OH_N,OH_S)
#print(UA_N,UA_S)
#print(MQ_N,MQ_S)
#print(AS_N,AS_S)
#print(F9_N,F9_S)
#print(HA_N,HA_S)
#não existe nenhum caso estremo vamo pra ponta do lapiz calcular a entropia da classe, para isso vou ter que tirar de cada variavel e bem já estou sem criatividade pra nomes atualmente são 3:00 da madruga :) vou mentir não que to me perdendo todo kkkkkkkkk
#observação vou fazer um pequeno ajuste tecnico pois eu percebi que não fiz uma varivel que contem a quantidade total de casos de uma unica companhia *-*

entropia_DL = -((dl_S/DL) * math.log2(dl_S/DL) + (dl_N/DL) * math.log2(dl_N/DL))
entropia_OO = -((OO_S/OO) * math.log2(OO_S/OO) + (OO_N/OO) * math.log2(OO_N/OO))
entropia_B6 = -((B6_S/B6) * math.log2(B6_S/B6) + (B6_N/B6) * math.log2(B6_N/B6))
entropia_US = -((US_S/US) * math.log2(US_S/US) + (US_N/US) * math.log2(US_N/US))
entropia_FL = -((FL_S/FL) * math.log2(FL_S/FL) + (FL_N/FL) * math.log2(FL_N/FL))
entropia_WN = -((WN_S/WN) * math.log2(WN_S/WN) + (WN_N/WN) * math.log2(WN_N/WN))
entropia_CO = -((CO_S/CO) * math.log2(CO_S/CO) + (CO_N/CO) * math.log2(CO_N/CO))
entropia_AA = -((AA_S/AA) * math.log2(AA_S/AA) + (AA_N/AA) * math.log2(AA_N/AA))
entropia_YV = -((YV_S/YV) * math.log2(YV_S/YV) + (YV_N/YV) * math.log2(YV_N/YV))
entropia_EV = -((EV_S/EV) * math.log2(EV_S/EV) + (EV_N/EV) * math.log2(EV_N/EV))
entropia_XE = -((XE_S/XE) * math.log2(XE_S/XE) + (XE_N/XE) * math.log2(XE_N/XE))
entropia__9E = -((_9E_S/_9E) * math.log2(_9E_S/_9E) + (_9E_N/_9E) * math.log2(_9E_N/_9E))
entropia_OH = -((OH_S/OH) * math.log2(OH_S/OH) + (OH_N/OH) * math.log2(OH_N/OH))
entropia_UA = -((UA_S/UA) * math.log2(UA_S/UA) + (UA_N/UA) * math.log2(UA_N/UA))
entropia_MQ = -((MQ_S/MQ) * math.log2(MQ_S/MQ) + (MQ_N/MQ) * math.log2(MQ_N/MQ))
entropia_AS = -((AS_S/AS) * math.log2(AS_S/AS) + (AS_N/AS) * math.log2(AS_N/AS))
entropia_F9 = -((F9_S/F9) * math.log2(F9_S/F9) + (F9_N/F9) * math.log2(F9_N/F9))
entropia_HA = -((HA_S/HA) * math.log2(HA_S/HA) + (HA_N/HA) * math.log2(HA_N/HA))


#aqui só foi pra eu me achar que eu me perdi e utilizei a ia pra escrever pra mim pq a coragem tava 10
#print("Entropia para DL:", entropia_DL)
#print("Entropia para OO:", entropia_OO)
#print("Entropia para B6:", entropia_B6)
#print("Entropia para US:", entropia_US)
#print("Entropia para FL:", entropia_FL)
#print("Entropia para WN:", entropia_WN)
#print("Entropia para CO:", entropia_CO)
#print("Entropia para AA:", entropia_AA)
#print("Entropia para YV:", entropia_YV)
#print("Entropia para EV:", entropia_EV)
#print("Entropia para XE:", entropia_XE)
#print("Entropia para OH:", entropia_OH)
#print("Entropia para UA:", entropia_UA)
#print("Entropia para MQ:", entropia_MQ)
#print("Entropia para AS:", entropia_AS)
#print("Entropia para F9:", entropia_F9)
#print("Entropia para HA:", entropia_HA)
#print("Entropia para 9E:", entropia__9E)
#print(entropia)


# curiosidade o \ no python é pra dizer que continua na proxima linha 
total_compania = ((DL)/numero_de_linhas) * entropia_DL + \
                 ((OO)/numero_de_linhas) * entropia_OO + \
                 ((B6)/numero_de_linhas) * entropia_B6 + \
                 ((US)/numero_de_linhas) * entropia_US + \
                 ((FL)/numero_de_linhas) * entropia_FL + \
                 ((WN)/numero_de_linhas) * entropia_WN + \
                 ((CO)/numero_de_linhas) * entropia_CO + \
                 ((AA)/numero_de_linhas) * entropia_AA + \
                 ((YV)/numero_de_linhas) * entropia_YV + \
                 ((EV)/numero_de_linhas) * entropia_EV + \
                 ((_9E)/numero_de_linhas) * entropia__9E + \
                 ((OH)/numero_de_linhas) * entropia_OH + \
                 ((UA)/numero_de_linhas) * entropia_UA + \
                 ((MQ)/numero_de_linhas) * entropia_MQ + \
                 ((AS)/numero_de_linhas) * entropia_AS + \
                 ((F9)/numero_de_linhas) * entropia_F9 + \
                 ((HA)/numero_de_linhas) * entropia_HA

print("Total Compania:", total_compania)
pureza = entropia - total_compania
print(entropia)
print(pureza)
