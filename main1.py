#lab3.1
from random import randint
k = 0
while k != 3:
    a = randint(1, 100)
    b = randint(1, 100)
    print(a, '+', b, '= ')
    c = int(input())
    if c == a + b:
        print('good, mistakes: ', k)
    else:
        k += 1
        print('bad, mistakes: ', k)