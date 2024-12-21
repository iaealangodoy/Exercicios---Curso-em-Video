l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
ar = l * a
t = ar / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m². \nPara pintar essa parede, você precisará de {}l de tinta.'.format(l, a, ar, t))