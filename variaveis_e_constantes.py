"""Em python possuimos variaveis e também constantes, a diferença entre elas é 
que as variaveis podem ter seus valores mutaveis e as constantes não, no python
diferente de outras linguagens não temos uma palavra reservada para definir uma
constante, como acontece no Java com uso da palavra final, para o python é usada
uma convenção, que é criar a 'variavel' com todas as letras maiusculas, abaixo
segue alguns exemplos."""

# Variaveis
numero = 10
nome = "Carlos"

print("o numero é: ",numero, "e o nome é: ",nome)

numero = 25
nome = "Fernanda"

print("o numero é: ",numero, "e o nome é: ",nome)

# Constantes

DEBUG = True
STATES = ['SP','RJ','MG']

AMOUNT = 30.2

print(DEBUG, STATES, AMOUNT)

"""No Python diferente das outras linguagens essas constantes são mutaveis
porém seguindo a convenção, ninguem altera estes valores"""