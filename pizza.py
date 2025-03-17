import pandas as pd
import matplotlib.pyplot as plt


dados = pd.read_csv("dados_agricolas.csv")


produtividade_por_cultivo = dados.groupby("tipo_de_cultivo")["produtividade"].sum()


plt.figure(figsize=(12, 8))
plt.pie(produtividade_por_cultivo, labels=produtividade_por_cultivo.index, autopct='%1.1f%%', 
        startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6', '#c2c2f0','#48D1CC','#32CD32','#808000','#4B0082'])


plt.title("Distribuição da Produtividade por Tipo de Cultivo", fontdict={'family': 'Arial', 'fontsize': 14, 'fontweight': 'bold'})


plt.show()

