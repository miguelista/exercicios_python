#obtendo números. o try, if e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado
while True:
    try:
        angulo1 = float(input("Passe o valor do primeiro ângulo\n"))
        if angulo1 >= 178:
            print("O ângulo não pode ter valor igual ou maior do que 178!")
            continue
        elif angulo1 <= 0:
            print("O ângulo não pode ter valor igual ou menor do que 0!")
            continue
        break
    except:
        print("Não é um número!")
    
while True: 
    try:
        angulo2 = float(input("Passe o valor de outro número...\n"))
        if (angulo1 + angulo2) >= 179:
            print("A soma dos ângulos não pode ter valor igual ou maior do que 179!")
            continue
        elif angulo2 <= 0:
            print("O ângulo não pode ter valor igual ou menor do que 0!")
            continue
        break
    except:
        print("Não é um número!")


print("O primeiro ângulo é ", angulo1)
print("O segundo ângulo é ", angulo2)
print("A soma dos ângulos é", (angulo1 + angulo2), " graus")



print("O Valor do terceiro ângulo é ",(180 - (angulo1 + angulo2)))



#mecanismo de saida
input("aperte enter para sair \n")
