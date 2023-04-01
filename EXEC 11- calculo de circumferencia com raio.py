#obtendo números. o while try e o break fazem com que o processo se repita até
#obtermos um número
while True:
    try:
        raio = float(input("Passe o valor do raio...\n"))
        if raio <= 0:
            print("O raio não pode ser menor ou igual a zero!")
            continue
        break
    except:
        print("Não é um número real!")
    


print("O raio é ", raio)
print("Então a circumferência é ", (raio * 3.14 * 2))



#mecanismo de saida
input("aperte enter para sair \n")
