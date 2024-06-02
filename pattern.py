#magik
c = 7
[print(' ' * (c - a) + '*' + ' ' * (a*2 - 1) + '*' * (a and 1)) for a in map(int, '0' + str(int('1' * (c - 1))**2) + '0')]