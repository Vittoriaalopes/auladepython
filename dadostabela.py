import matplotlib.pyplot as plt

#dados extraidos da tabela fao.org
paises = ["Brasil", "México"]
consumo = [21.6, 34.2]  # percentual de mulheres que consomem ovos

#criar o grafico de pizza
plt.figure(figsize=(8, 8))
plt.pie(consumo, labels=paises, autopct="%.1f%%", colors=["blue", "red"], startangle=90)

# titulo do grafico
plt.title("Consumo de Ovos por Mulheres (%)")

#mostra o graico
plt.show()


