import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')


plt.figure(figsize=(10, 10))
for column in ['Durata', 'Puls', 'MaxPuls', 'Calorii']:
    plt.plot(df.index, df[column], label=column, marker='x',)

plt.title('All Values')
plt.legend()
plt.show()

plt.figure(figsize=(10, 10))
for column in ['Durata', 'Puls']:
    plt.plot(df.index[:4], df[column][:4], label=column, marker='x')

plt.title('First 4 Values')
plt.legend()
plt.show()

ult = df[['Durata', 'Puls']].tail(7)
plt.figure(figsize=(10, 10))
for column in ['Durata', 'Puls']:
    plt.plot(ult.index, ult[column], label=column, marker='x')

plt.title('Last 7 Values')
plt.legend()
plt.show()



