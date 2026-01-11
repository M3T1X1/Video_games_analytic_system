import pandas as pd

data = pd.read_csv('vgchartz-2024.csv')

#data.drop(columns=['img'], inplace=True) #usunięcie kolumny "img"
#data.drop(columns=['last_update'], inplace=True) #usunięcie kolumny "last_update"
data.dropna(subset=['critic_score'], inplace=True) #usunięcie wierszy gdzie critic_score jest puste

data.to_csv('vgchartz-2024.csv', index=False)