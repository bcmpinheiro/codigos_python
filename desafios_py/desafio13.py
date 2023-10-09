salarioAtual = float(input('Digite o valor do seu salário: '))
salarioComAumento = salarioAtual + (salarioAtual * 15 / 100)
print('Você recebeu um aumento de 15 porcento e seu salario era R${:.2f} reais e passará a ser R${:.2f} reais!'.format(salarioAtual, salarioComAumento))