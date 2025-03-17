def contar(palavra):
    vogais = 'aeiou'
    conta = 0
    for vogal in palavra:
        if vogal in vogais:
            conta+=1
    return conta

palavra = str(input('Digite a palavra:'))

print(contar(palavra))