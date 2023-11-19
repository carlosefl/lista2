import pandas as pd
import math

banco =  pd.read_csv('airlines_delay.csv')


numero_de_linhas = banco.shape[0]

print(numero_de_linhas + 2)