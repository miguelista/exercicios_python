#obtendo números. o try e o break fazem com que o processo se repita até
#obtermos um número
while True:
    try:
        numero1 = float(input("Passe o valor de um número real...\n"))
        break
    except:
        print("Não é um número!")
    
while True: 
    try:
        numero2 = float(input("Passe o valor de outro número...\n"))
        break
    except:
        print("Não é um número!")


print("O primeiro número é ", numero1)
print("O segundo número é ", numero2)

#compara os números e faz a conta de acordo
if numero1 > numero2:
    print("A diferença dos valores dados é ", (numero1 - numero2))
else:
    print("A diferença dos valores dados é ", (numero2 - numero1))


#mecanismo de saida
input("aperte enter para sair \n")
