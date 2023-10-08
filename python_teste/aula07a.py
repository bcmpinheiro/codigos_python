nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoint = n1 // n2
exponencial = n1**n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
print('Divisão inteira {} e potência {}'.format(divisaoint, exponencial))