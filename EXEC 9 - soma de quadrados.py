while True:
    try:
        numero1 = int(input("Passe o valor de um número inteiro...\n"))
        break
    except:
        print("Não é um número inteiro!")
    
while True: 
    try:
        numero2 = int(input("Passe o valor de outro inteiro...\n"))
        break
    except:
        print("Não é um número inteiro!")


print("O quadrado do primeiro número é ", (numero1 ** 2))
print("O quadrado do segundo número é ", (numero2 ** 2))

print("A soma dos quadrados é ", ((numero2 ** 2) + (numero1 ** 2)))



input("aperte enter para sair \n")
