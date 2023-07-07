"""INTERPOLAÇÃO DE STRINGS"""

nome = "lexeba"
idade = 28
profissao = "Pedreiro"
linguagem = "Cimento"
saldo = 45.435

dados = {"nome": "Lexeba", "idade": 18}

PI = 3.14159

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(idade=idade, nome=nome))
print("Nome: {name} Idade: {age} {age} {name}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")
print(f"Valor de PI: {PI:10.2f}")
