# E, utiliza-se and
# OU, utiliza-se or
# NEGAÇÃO, utiliza-se o not
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

print("\n========== Exemplos ==========")
saldo = 1000
saque = 250
limite = 200
conta_especial = True

contatos_emergencia = []  # Lista vazia

print(not contatos_emergencia)


exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (
    conta_especial and saldo >= saque)
print(exp_2)
