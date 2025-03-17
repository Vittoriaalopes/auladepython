import pandas as pd 
import matplotlib.pyplot as plt 
# Carregando os dados 
dados_produtos = pd.read_csv('produtos.csv',delimiter=',') 
print(dados_produtos.columns) 
# Criando o gráfico de PRECO por ANO para cada PRODUTO 
plt.figure(figsize=(10, 6)) 
# Plotando os dados para cada produto 
for produto in dados_produtos['produtos'].unique(): 
    dados_produto = dados_produtos[dados_produtos['produtos'] == produto] 
    plt.plot(dados_produto['ano'], dados_produto['preco'], label=produto, marker='o')
    
# Adicionando título e rótulos 
plt.title('Preço dos Produtos ao Longo dos Anos') 
plt.xlabel('Ano') 
plt.ylabel('Preco') 
plt.legend(title='Produtos') 
# Exibindo o gráfico 
plt.grid(True) 
plt.show() 
