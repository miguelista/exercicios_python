#importando modulo necessário
import math

#obtendo números. o try, if e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado
while True:
    try:
        cateto1 = float(input("Passe o valor do primeiro cateto\n"))
        if cateto1 <= 0:
            print("O cateto não pode ter valor igual ou menor do que 0!")
            continue
        break
    except:
        print("Não é um número!")
    
while True:
    try:
        cateto2 = float(input("Passe o valor do segundo cateto\n"))
        if cateto2 <= 0:
            print("O cateto não pode ter valor igual ou menor do que 0!")
            continue
        break
    except:
        print("Não é um número!")



print("O primeiro cateto é ", cateto1)
print("O segundo cateto é ", cateto2)
print("Os quadrados dos catetos são ", (cateto1 ** 2), " e ", (cateto2 ** 2))



print("O Valor da hipotenusa  é ",(math.sqrt((cateto1 ** 2) + (cateto2 ** 2))))



#mecanismo de saida
input("aperte enter para sair \n")
