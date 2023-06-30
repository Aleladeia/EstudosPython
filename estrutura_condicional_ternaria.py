"""
IF Ternário nos permite escrever uma condição em
uma unica linha ele é composto por três partes a
primeira é o retorno caso a expressão retorne
verdadeiro, a segunda é a expressão lógica e a
terceira parte é o retorjo caso a expressão não
seja atendida.
"""
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")
