import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder


df =  pd.read_csv('airlines_delay.csv')

label_encoder = LabelEncoder()
df['Airline'] = label_encoder.fit_transform(df['Airline'])
df['AirportFrom'] = label_encoder.fit_transform(df['AirportFrom'])
df['AirportTo'] = label_encoder.fit_transform(df['AirportTo'])

# Selecionando as colunas relevantes para o clustering
features = ['Flight', 'Time', 'Length', 'Airline', 'AirportFrom', 'AirportTo', 'DayOfWeek']

# Aplicando o K-Means
kmeans = KMeans(n_clusters=2, random_state=42)  # Você pode ajustar o número de clusters conforme necessário
df['Cluster'] = kmeans.fit_predict(df[features])

# Visualizando os resultados
print(df[['Flight', 'Time', 'Length', 'Airline', 'AirportFrom', 'AirportTo', 'DayOfWeek', 'Cluster']])
