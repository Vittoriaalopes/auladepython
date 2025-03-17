produto = {
    'Nome': ['Feijão','ingá','Ramutã'], 
    'Quantidade': [9, 10, 400], 
    'Preço': [5, 4, 80]
}

#for chave, valor in produto.items():
 #   print(chave, valor)
for a,b,c in zip(produto['Nome'],produto['Quantidade'],produto['Preço']):
    print("Produto: ",a,"Quantidade: ",b," Preço: ",c)
