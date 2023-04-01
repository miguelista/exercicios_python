

#obtendo números. o try, if e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado

#eu poderia transformar essas perguntas numa unica função, mas isso vem depois.
while True:
    try:
        mins_percurso = int(input("Digite os minutos de viagem \n"))
        if mins_percurso <= 0:
            print("Não é possível viajar por 0 minutos ou menos!")
            continue
        break
    except:
        print("Não é um número!")


while True:
    try:
        velocidade_media = float(input("Digite a velocidade média em Km/h \n"))
        if velocidade_media <= 0:
            print("Não é posssível ficar parado ou dirigir para trás!")
            continue
        break
    except:
        print("Não é um número!")



#checando e reportando os dados recebidos
print("\nAs horas de viagem são ", (mins_percurso / 60))
print("A velocidade média é ", velocidade_media, " Km/h")
print("O percurso corrido foi de ", ((mins_percurso / 60) * velocidade_media), "Kilômetros \n")

#resultado
print("Os litros gastos na viagem foram ", ((((mins_percurso / 60) * velocidade_media)) / 12), " litros \n")


#mecanismo de saida
input("\naperte enter para sair \n")
