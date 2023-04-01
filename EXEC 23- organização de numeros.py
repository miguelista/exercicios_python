#importando modulo necessário
import math

#obtendo números. o try, if e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado

print("Serão recebidos 3 valores em ordem crescentes, e um ultimo valor aleatório. ",
    "Este programa organizaram os 4 valores em ordem crescente. \n")
#eu poderia transformar essas perguntas numa unica função, mas isso vem depois.

while True:
    try:
        numero_1 = float(input("Digite o primeiro número\n"))
        break
    except:
        print("Não é um número!")


while True:
    try:
        numero_2 = float(input("\nDigite o segundo número; ele precisa ser maior do que o primeiro\n"))
        if numero_2 < numero_1:
            print("O número não pode ser menor do que seu antecedente")
            continue
        break
    except:
        print("Não é um número!")


while True:
    try:
        numero_3 = float(input("\nDigite o terceiro número; ele precisa ser maior que seu antecedente\n"))
        if numero_3 < numero_2:
            print("O número não pode ser menor do que seu antecedente")
            continue
        break
    except:
        print("Não é um número!")    


while True:
    try:
        numero_extra = float(input("\nDigite o quarto número; ele pode ter qualquer valor\n"))
        if numero_extra == numero_1 or numero_extra == numero_2 or numero_extra == numero_3:
            print("O número extra não pode ser igual aos outros números")
            continue
        break
    except:
        print("Não é um número!")
        

#resultados
if numero_extra > numero_3:
    print("\nOs números recebidos, em ordem crescente, foram: \n",
    numero_1, ";", numero_2, ";", numero_3, "e", numero_extra)
    
elif numero_extra > numero_2:
    print("\nOs números recebidos, em ordem crescente, foram: \n",
    numero_1, ";", numero_2, ";", numero_extra, "e", numero_3)

elif numero_extra > numero_1:
    print("\nOs números recebidos, em ordem crescente, foram: \n",
    numero_1, ";", numero_extra, ";", numero_2, "e", numero_3)

else:
    print("\nOs números recebidos, em ordem crescente, foram: \n",
    numero_extra, ";", numero_1, ";", numero_2, "e", numero_3)


#mecanismo de saida
input("\naperte enter para sair \n")
