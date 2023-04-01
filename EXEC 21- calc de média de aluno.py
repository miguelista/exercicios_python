#importando modulo necessário
import math

#obtendo números. o try, if e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado

print("Digite 4 notas bimestrais de um aluno. será calculado sua média e classificação final. \n")
#eu poderia transformar essas perguntas numa unica função, mas isso vem depois.

while True:
    try:
        nota_1 = float(input("Digite a primeira nota bimestral \n"))
        if nota_1 < 0 or nota_1 > 10:
            print("Não é possível a nota ser menor que 0 ou maior que 10")
            continue
        break
    except:
        print("Não é um número!")


while True:
    try:
        nota_2 = float(input("Digite a segunda nota bimestral\n"))
        if nota_2 < 0 or nota_1 > 10:
            print("Não é possível a nota ser menor que 0 ou maior que 10")
            continue
        break
    except:
        print("Não é um número!")


while True:
    try:
        nota_3 = float(input("Digite a terceira nota bimestral\n"))
        if nota_3 < 0 or nota_1 > 10:
            print("Não é possível a nota ser menor que 0 ou maior que 10")
            continue
        break
    except:
        print("Não é um número!")    


while True:
    try:
        nota_4 = float(input("Digite a quarta nota bimestral\n"))
        if nota_4 < 0 or nota_1 > 10:
            print("Não é possível a nota ser menor que 0 ou maior que 10")
            continue
        break
    except:
        print("Não é um número!")
        

#checando e reportando os dados recebidos
print("\nAs notas recebidas foram ", nota_1, ", ", nota_2, ", ", nota_3, "e ", nota_4)


#resultados
nota_final = ((nota_1 + nota_2 + nota_3 + nota_4) / 4)
print("\nA média final é ", nota_final, "\n")

if nota_final >= 6:
    print("O aluno teve uma nota igual ou superior a 6; ele foi aprovado")
elif nota_final >= 3 and nota_final < 6:
    print("O aluno teve uma nota entre 3 e 6; ele será encaminhado a um exame de aproveitamento")
else:
    print("A nota do aluno foi inferior a 3; ele foi retido")


#mecanismo de saida
input("\naperte enter para sair \n")
