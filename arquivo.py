import pandas as pd 
dadosProdutos = pd.read_csv("produtos.csv")
print(dadosProdutos.columns)
 
dadosProdutos['preco'].max() 
print("Média de Preços dos Produtos ", dadosProdutos['preco'].mean()) 