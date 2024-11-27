import random
x = random.randint(3, 20)
def password():
    numb = []
    i = 1
    j = 2
    while i < j:
        for i in range(1, x):
            for j in range(1, x):
                if i >= j:
                    continue
                if i + j == x or x % (i + j) == 0:
                    numb.append(i)
                    numb.append(j)
                    continue
        return numb
print('Число из первой вставки:', x)
print('Пароль для второй вставки:', *password())
    