

#obtendo números. o try, if e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado

#eu poderia transformar essas perguntas numa unica função, mas isso vem depois.
while True:
    try:
        numero_1 = int(input("Digite um número inteiro \n"))
        break
    except:
        print("Não é um inteiro!")


while True:
    try:
        numero_2 = int(input("Digite outro inteiro\n"))
        break
    except:
        print("Não é um inteiro!")



#checando e reportando os dados recebidos
print("\nOs números recebidos são ", numero_1, " e ", numero_2, "\n")

#resultado
if numero_1 > numero_2:
    print(numero_1, " é o número maior. A diferença entre ele e ", numero_2, " é ", (numero_1 - numero_2))
else:
    print(numero_2, " é o número maior. A diferença entre ele e ", numero_1, " é ", (numero_2 - numero_1))


#mecanismo de saida
input("\naperte enter para sair \n")
