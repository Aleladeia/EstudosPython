nome = input("informe o seu nome: ")
idade = input("informe sua idade: ")


print(nome, idade)
# define o fim da string, por padrão o end é o \n sem precisar
# informalo como no exemplo acima, ele ja pula a linha se formos
# definir um end personalizado se não colocarmos um \n ele não
# quebra a linha
print(nome, idade, end="...\n")
print(nome, idade, "end modificado fica assim sem o \ n ", end="...")
print(nome, idade, "com o \ n ", end="\n")
# define o separador entre as variaveis, substitui os espaços em branco
print(nome, idade, sep="#")

# podemos usar o seperador e end modificados também
print(nome, idade, sep="#", end="bololo\n")
