opcao = -1


# utilizamos o while quando não sabemos a quantidade de execuções que o
# código vai ter.
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo Extrato...")
# Novamente o else não é comumente utilizado, é mais para saber que a
# opção de utilizalo existe.
else:
    print("Obrigado por usar nosso sistema, tenha um bom dia.")
