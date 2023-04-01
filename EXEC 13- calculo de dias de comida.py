#obtendo números. o try e o break fazem com que o processo se repita até
#obtermos um número
while True:
    try:
        comida = int(input("Digite quantos kilos de comida tem...\n"))
        if comida <= 0:
            print("Não é possivel ter 0 kilos ou menos!")
            continue 
        break
    except:
        print("Não é um número inteiro!")


print("Você tem ", comida, " kilos de comida, ou...")  
comida = comida * 1000
print( comida, " gramas de comida")


print("Assumindo que você coma 500 gramas por dia, você terá comida por", int(comida / 500), " dias")



#mecanismo de saida
input("aperte enter para sair \n")
