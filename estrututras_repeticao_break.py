
# Exemplo abaixo é um loop infinito e para cortar o laço
# colocamos uma condição que se for atendida, atraves do valor
# 10 informado que entrando no if executa o break que corta o laço
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break  # break é utilizado para cortar o laço de repetição

    if numero % 2 == 0:
        continue

    print(numero)


for numero in range(100):

    if numero == 12:
        continue  # continue é utilizado quando queremos pular uma execução

    print(numero, end=" ")
