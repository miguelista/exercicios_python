#obtendo números. o try e o break fazem com que o processo se repita até
#obtermos um número
while True:
    try:
        ano_nascimento = int(input("Digite o ano de seu nascimento...\n"))
        break
    except:
        print("Não é um número inteiro!")
    
while True: 
    try:
        ano_atual = int(input("Digite o ano atual...\n"))
        if ano_atual <= ano_nascimento:
            print("O ano atual não pode ser menor ou igual ao ano de nascimento!")
            continue
        break
    except:
        print("Não é um número inteiro!")


print("O ano de nascimento é ", ano_nascimento)
print("O ano anual é ", ano_atual)



print("A idade do usuário é ", (ano_atual - ano_nascimento))
print("O usuário terá", ((ano_atual - ano_nascimento) + 17), " daqui a 17 anos")



#mecanismo de saida
input("aperte enter para sair \n")
