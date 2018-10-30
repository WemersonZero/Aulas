n1 = int(input('Uma valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2
print('A soma é {},\n o produuto é {} e a \n divisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
