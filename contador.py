arquivo = open('texto.txt', 'r')
def contar(palavra):
    vogais = 'aeiou'
    contar = 0
    for vogal in palavra:
        if vogal in vogais:
            contaq+=1
    return contar
palavra = str(input("Digite a palavra: "))
print(contar(palavra))
for linha in arquivo:
    print(linha)
    arquivo.close()