largura = float(input('Digite a largura em mts de uma parede: '))
altura = float(input('Digite a altura em mts de uma parede: '))
area = largura * altura
lataTinta = 1 * 2
pintura = area / lataTinta
print('A largura da parede é {} mts \nA altura da parede é {} mts \nSerão necessárias {} latas de tinta por m2'.format(largura, altura, pintura))
