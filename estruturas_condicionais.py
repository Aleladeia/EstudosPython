"""
  O que vamos aprender?
   - if/ if-else/ elif
   - if aninhado
   - if ternário

   CONTINUAR AULA A PARTIR DOS 16 MINUTOS #F016
"""

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

print(" ========= Utilizando varios ifs ========= ")
if idade >= MAIOR_IDADE:
    print("Pode tirar CNH pois é maior de idade")

if idade < MAIOR_IDADE:
    print("Não pode tirar CNH, você é menor de 18 ainda :c")

print(" \n========= Utilizando if e else ========= ")
if idade >= MAIOR_IDADE:
    print("Pode tirar CNH pois é maior de idade")
else:
    print("Não pode tirar CNH, você é menor de 18 ainda :c")

print(" \n========= Utilizando elif ========= ")
# O elif é apenas uma abreviação do else if
if idade >= MAIOR_IDADE:
    print("Pode tirar CNH pois é maior de idade")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas praticas")
else:
    print("Não pode tirar CNH, você é menor de 18 ainda :c")
