palavra = str(input("insira uma palavra:  ")) #declaração da variavel

if palavra == palavra[::-1]: #verificação da palavra escrita normalmente é igual == a palavra invertida [::-1]
    print(f"palavra '{palavra}' é um palindromo")
else:
    print(f"palavra '{palavra}' não é um palindromo")