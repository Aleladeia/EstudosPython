texto = input("informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha
    print("Executa no final do código")


#  O Else no lasso for não é comumente usado, mas existe.

# Exemplo utilizando função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
