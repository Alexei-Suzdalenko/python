from asyncio import exceptions


x = 0

try:
    y = 11 / x
except:
    print('!!! error ocurried !!!')

print(x)