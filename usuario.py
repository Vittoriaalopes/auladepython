def ti (login, senha):
    return login == "admin" and senha == "admin"

login = str (input("Digite o login: "))
senha = str (input("Digite a senha: "))

print(ti(login, senha))