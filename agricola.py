import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dados_agricolas.csv")

dados.columns = dados.columns.str.strip()

print(dados.head())

#tipo de cultivo e calcular a produtividade media
produtividade_media = dados.groupby("tipo_de_cultivo")["produtividade"].mean().reset_index()
print("\nProdutividade média por tipo de cultivo:")
print(produtividade_media)

# produto com maior produtividade media
produto_max_produtividade = produtividade_media.loc[produtividade_media["produtividade"].idxmax()]
print("\nProduto com maior produtividade:")
print(produto_max_produtividade)

#  menor uso medio de água
uso_agua_medio = dados.groupby("tipo_de_cultivo")["uso_de_agua"].mean()
produto_min_uso_agua = uso_agua_medio.idxmin()
print("\nProduto com menor uso médio de água:", produto_min_uso_agua)


plt.figure(figsize=(10, 6))
sns.lineplot(data=dados, x="ano", y="produtividade", hue="tipo_de_cultivo", marker="o")


plt.title("Produtividade ao longo dos anos por tipo de cultivo")
plt.xlabel("Ano")
plt.ylabel("Produtividade (Toneladas por Hectare)")
plt.legend(title="Tipo de Cultivo")
plt.grid(True)
plt.show()
