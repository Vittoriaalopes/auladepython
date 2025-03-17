# Coloquei meu nome em realce e pra isso criei essa função
def borda(s1):
    tam = len(s1)
    if tam:
        print('+','-' * tam,'+')
        print('|','Vittoria de Castro Amorim Lopes','|')
        print('+','-' * tam, '+')
print('Olá! Seja muito bem vindo(a) a lojinha de t-shirts da')
borda('Vittoria de Castro Amorim lopes')
print('Promoção de t-shirts!!!! \n')
# Criação das variáveis
valor = float(input('Insira o valor da t-shirt: '))
quantidade = int(input('Insira a quantidade de t-shirt: '))
# Condição para os decontos
if quantidade < 10:
    desconto = 0
elif quantidade < 20:
    desconto = 0.1
else:
    desconto = 0.2
# Parametros para os valores
valor_sem_desconto = quantidade * valor
valor_com_desconto = valor * (1 - desconto)
valor_total = quantidade * valor_com_desconto
valor_desconto = quantidade * valor * desconto
porcentagem_desconto = desconto * 100
# Sáida dos dados
print(f'Valor total sem desconto: ', valor_sem_desconto)
print(f'Valor unitário: R$ {valor:.2f}')
print(f'Valor com desconto: R$ {valor_total:.2f} ({porcentagem_desconto:.0f}% de desconto)')
print(f'Valor total: R$ {valor_total:.2f} (desconto total: R$ {valor_desconto:.2f})')
