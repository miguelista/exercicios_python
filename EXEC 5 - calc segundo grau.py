import math
#variaveis
const_a = float(input("insira o valor da constante A \n"))
const_b = float(input("insira o valor da constante B \n"))
const_c = float(input("insira o valor da constante C \n"))

#tentando delta
try:
    delta = ((const_b**2)-(4*const_a+const_c))/(2*const_a)
    print("delta é ", delta)
    print("a raiz de delta é ", math.sqrt(delta))

except:
    print("delta tem valor negativo! não é possível fazer a operação. \n dica: tente aumentar o valor de B")

#resto do código
else:
    resultado1 = (-abs(const_b))+ (math.sqrt(delta))
    resultado2 = (-abs(const_b))- (math.sqrt(delta))
    
    print("O valor de X pode ser ", resultado1, " ou ", resultado2)


    input("aperte enter para sair \n")
