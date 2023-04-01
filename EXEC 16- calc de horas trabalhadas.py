#importando modulo necessário
import math

#obtendo números. o try, if e o break fazem com que o processo se repita até
#obtermos um número que possa ser utilizado

#eu poderia transformar essas perguntas numa unica função, mas isso vem depois.
while True:
    try:
        horas_trabalho = int(input("Digite as horas de trabalho\n"))
        if horas_trabalho <= 0:
            print("Não é posssível trabalhar por 0 horas ou menos!")
            continue
        break
    except:
        print("Não é um número!")


while True:
    try:
        valor_hora = float(input("Passe o valor do recebido por hora \n"))
        if horas_trabalho <= 0:
            print("Não é posssível receber 0 ou menos por hora!")
            continue
        break
    except:
        print("Não é um número!")


while True:
    try:
        valor_desconto = float(input("Passe o valor do desconto \n"))
        if valor_desconto < 0:
            print("Não é possível ter um desconto negativo!")
            continue
        break
    except:
        print("Não é um número!")  
    

while True:
    try:
        numero_dependentes = int(input("Digite o número de dependentes\n"))
        if numero_dependentes < 0:
            print("Não é possível ter menos do que 0 dependentes!")
            continue
        break
    except:
        print("Não é um número!")


#checando e reportando os dados recebidos
print("\nAs horas de trabalho são ", horas_trabalho)
print("O valor recebido por hora é ", valor_hora)
print("O valor  de desconto é ", valor_desconto)
print("O número de dependentes é ", numero_dependentes, "\n")


#resultados
print("O salário bruto é ",(horas_trabalho * valor_hora), " reais.")
print("O salário líquido é ", ((horas_trabalho * valor_hora) - valor_desconto), "reais.")
print("É acrescido 100 reais ao salario líquido por cada dependente;\n")
print("Logo o valor final do salário é...")
print((((horas_trabalho * valor_hora) - valor_desconto) + (numero_dependentes * 100)), " reais.")


#mecanismo de saida
input("\naperte enter para sair \n")
