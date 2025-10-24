# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

# Se o usuário e a senha estão corretos → "Login bem-sucedido"

# Senão → "Usuário ou senha incorretos"

dados = {
    "user":"icaro450",
    "senha":"senha1234"
}
login = {

}
login["user"] = str(input("Qual seu usuário? "))
login["senha"] = str(input("Qual sua senha? "))

if login["user"] == dados["user"] and login["senha"] == dados["senha"]:
    print("Login bem-sucedido")
else:
    print("Usuário ou senha incorretos")