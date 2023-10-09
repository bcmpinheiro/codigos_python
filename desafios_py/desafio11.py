largura = float(input('Digite a largura em mts de uma parede: '))
altura = float(input('Digite a altura em mts de uma parede: '))
area = largura * altura
lataTinta = 1 * 2
pintura = area / lataTinta
print('Sua parede tem {} x {} e sua área é {}m² \nSerão necessárias {}l de tinta.'.format(largura, altura, area, pintura))
