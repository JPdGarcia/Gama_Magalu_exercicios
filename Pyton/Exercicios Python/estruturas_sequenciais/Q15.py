#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:


print("Vamos calcumar o seu salario mensal ")
porHora = input("Quanto você ganha por hora trabalhada? ")
horas = input("Quantas horas você trabalha por mês? ")

valorPorHora = float(porHora)
horasTrabalhadas = float(horas)

salario = valorPorHora*horasTrabalhadas
ir = salario*0.11
inss = salario*0.08
sindicato = salario*0.05
liquido = salario-ir-inss-sindicato

print("O seu salario bruto é: ", salario)
print("Seu Imposto de Renda é: ", ir)
print("Sua contribuição para o INSS é: ", inss)
print("Sua contribuição para o Sindicato é: ", sindicato)
print("Seu salario liquido é: ", liquido)
