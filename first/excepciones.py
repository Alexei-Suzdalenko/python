import math as m

x = 0

try:
    y = 11 / x
    x = 'ok'
except:
    print('!!! error ocurried !!!')

print(x)

# excepciones propias

if x < 0:
    raise TypeError('mostramos un error particular')

print(m.sqrt(64))