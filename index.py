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

banco =  pd.read_csv('airlines_delay.csv')

# calculando a entropia principal com base no atraso e não atraso, sendo x atraso e y não atraso
for teste in banco['Class']:
    if teste == 1:
        x = x + 1
    else:
        y = y + 1


positivo = y/539382

negativo = x/539382


entropia = (-positivo * math.log2(positivo) - negativo * math.log2(negativo))

# começando a tratar as classes começando pela  Airline que é a companhia 

#o nunique vai ver todas as linhas e vai pegar as companias apenas uma vez mesmo que ela apareça varias vezes, isso é necessario para eu fazer o calculo do ganho da classe
companias = banco['Airline'].unique()

for i in companias:
    print(i)