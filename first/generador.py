# a mano 
from operator import ne


def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num * 2)
        num = num + 1
    return miLista

# print(generaPares(10))        


# generador construir un objeto iterable
def generaParesAdvance(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1
    


result = generaParesAdvance(10)

# print(next(result))
# print(result)
# print(next(result))
# print(next(result))
# 
# print('-------------------------------------')
# for i in result:
#     print(i)


# yield from
def dameCuidades(* cuidades):
    for city in cuidades:
        for letter in city:
            yield letter

cuidades_devueltas = dameCuidades('madrid', 'santander', 'paris', 'klintsy')

print(next(cuidades_devueltas))
print(next(cuidades_devueltas))


# yield from
def dameCuidades1(* cuidades):
    for city in cuidades:
        yield from city

cuidades_devueltas1 = dameCuidades1('madrid', 'santander', 'paris', 'klintsy')

print(next(cuidades_devueltas1))
print(next(cuidades_devueltas1))