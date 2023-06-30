print("============= Operações Matematicas =============\n")

# adicao
print(10 + 2, "  Adição de 10 + 2")

# subtração
print(10 - 5, "   Subtração de 10 - 5")

# multiplicação
print(3 * 2, "   Multiplicação de 3 x 2")

# divisão
print(10 / 2, " Divisão de 10/2")

# divisão inteira
print(10 // 2, "   Divisão inteira de 10/2")

# módulo, resto da divisão
print(10 % 3, "   Módulo de 10/3")

# potenciação
print(10 ** 2, " Potenciação de 10 elevado a 2")

"""Precedência
   De acordo com a matematica segue esta ordem

   Parentesis
   Expoente
   Multiplicações e divisões (da esquerda para a direita)
   Somas e Subtrações (da esquerda para a direita)

   Exemplos abaixo
"""

print("\n============= Operações com Precedência aplicada =============\n")

x = 10 + 5 * 4
print(x, "  <== resultado da expressão 10 + 5 x 4 = 30")

x = (10+5)*4
print(x, "  <== resultado da expressão (10 + 5) x 4 = 60")

y = 10 / 2 + 25 * 2 - 2 ** 2
print(y, "<== resultado da expressão 10 /2 + 25 * 2 - 2 **2 = 51.0")

y = (10 / 2) + (25 * 2) - (2 ** 2)
print(y, "<== resultado da expressão (10 / 2) + (25 * 2) - (2 ** 2) = 51.0")

y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(y, " <== resultado da expressão (10 / 2) + 25 * ((2 - 2) ** 2) = 5.0")
