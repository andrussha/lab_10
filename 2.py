'''
Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
Постолович А.С. 122-В
'''
import timeit
import random
import sys
i = input("Select the method of calculating\n"
          "Recursion - 1, Iteration - other symbol: ") #вибираємо метод - рекурсія чи ітерація
n = random.randint(1, 9999)
b = n


def Iteration(n): #заводимо функцію для обчислення факторіалу через ітерацію
    while n > 10:
        n1 = n//1000
        n2 = (n//100)%10
        n3 = (n%100)//10
        n4 = n%10
        n = n1 + n2 + n3 + n4
    return n

def Recursion(n): #заводимо функцію для обчислення факторіалу через рекурсію
    sys.setrecursionlimit(b+1)
    if n < 10:
        return n
    else:
        return Recursion(n%10 + Recursion(n//10))

rec_size = sys.getsizeof(Recursion(n)) #знаходимо розмір обох функцій
iter_size = sys.getsizeof(Iteration(n))

if i == '1':
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f'Digital root of {b} = {Recursion(n)}')
    print(f'The program lasted {t} seconds')
    print(f'The amount of occupied memory - {rec_size}')
else:
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f'Digital root of {b} = {Iteration(n)}')
    print(f'The program lasted {t} seconds')
    print(f'The amount of occupied memory - {iter_size}')