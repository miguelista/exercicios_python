

#obtendo números. o try e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado

#eu poderia transformar essas perguntas numa unica função, mas isso vem depois.
while True:
    try:
        numero_1 = float(input("Digite um número \n"))
        break
    except:
        print("Não é um número!")


while True:
    try:
        numero_2 = float(input("Digite outro número \n"))
        break
    except:
        print("Não é um número!")



#checando e reportando os dados recebidos
print("\nOs números recebidos são ", numero_1, " e ", numero_2, "\n")

#resultado
if numero_1 > numero_2:
    print(numero_1, " é o número maior.")
else:
    print(numero_2, " é o número maior.")


#mecanismo de saida
input("\naperte enter para sair \n")
