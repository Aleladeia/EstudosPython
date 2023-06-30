
print("=========== Inteiro para float ===========\n")

preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10/2
print(preco)

print("=========== Exibindo os tipos ===========\n")

valor = 10
valor_str = str(valor)

print(type(valor))
print(type(valor_str))

print("\n=========== Float para inteiro ===========\n")

preco = 10.3
print(preco)

preco = int(preco)
print(preco)

print("\n=========== Conversão por divisão ===========\n")

preco = 10
print(preco)

print(preco/2)
# com duas barras é feito uma divisão inteira
print(preco//2)

print("\n=========== Numérico para string ===========\n")

preco = 10.50
idade = 28

print(str(preco))
print(str(idade))
# utilizamos o f para dizer que vamos passar variaveis dentro da nossa string
# essa é uma das formas de concatenar
texto = f"idade: {idade} preco: {preco}"
print(texto)

print("\n=========== String para número ===========\n")

preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

print("\n=========== Erro de conversão ===========\n")
# segue exemplo de conversão de uma string de caracteres para float

preco = "python"
# esse tipo de conversão não funciona e nem deve funcionar pois python
#  não é um numero válido e sim uma sequencia de caracteres, uma palavra.
print(float(preco))

# mensagem retornada abaixo
""" Traceback (most recent call last):
  File "c:\wspython\CursoDIO\Projetos\conversao_de_tipos.py", line 56, in
    <module>
    print(float(preco))
          ^^^^^^^^^^^^
ValueError: could not convert string to float: 'python'"""
