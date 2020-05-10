import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

df_regions = pd.read_csv("./dati-regioni/dpc-covid19-ita-regioni.csv")
regioni = ["Veneto", "Friuli Venezia Giulia","Lombardia","Emilia-Romagna"]
colori = ["blue","green","red","black"]
toplot = "nuovi_positivi"


for i, regione in enumerate(regioni):
	fig, ax = subplots()
	a = df_regions.loc[df_regions['denominazione_regione'] == regione]
	a.plot(kind='line',x='data',y=toplot,color=colori[i], ax=ax)
	ax.set_title('Nuovi positivi')
	ax.grid()
	ax.legend([regione]);
plt.show()

df_nation = pd.read_csv("./dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
nat_pos = df_nation['nuovi_positivi']
nat_die = df_nation['deceduti']
data = df_nation['data']
figure()
plt.title("Nuovi positivi nazionali")
plt.grid()
plt.plot(data, nat_pos, color='red')
plt.show()
figure()
plt.title("Decessi nazionali")
plt.grid()
plt.plot(data, nat_die, color='black')
plt.show()

daily_die = []
d_d = []
for i in range(len(nat_die)):
    daily_die.append(nat_die[i])
    d_d.append(nat_die[i])

for i in range(1, len(daily_die)):
    daily_die[i] = daily_die[i] - d_d[i-1]
    
figure()
plt.title("Decessi giornalieri")
plt.grid()
plt.plot(data, daily_die, color='green')
plt.show()
