'''
Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
Постолович А.С. 122-В
'''
import sys
import timeit

n = int(input('Input number: ')) #вводимо число для обчислення факторіалу
i = input("Select the method of calculating the factorial\n"
          "Recursion - 1, Iteration - other symbol: ") #вибираємо метод - рекурсія чи ітерація
b = n

def Recursion(n): #заводимо функцію для обчислення факторіалу через рекурсію
    sys.setrecursionlimit(10000)
    if n == 0:
        return 1
    return Recursion(n-1)*n

def Iteration(n): #заводимо функцію для обчислення факторіалу через ітерацію
    factorial = 1
    while n >= 1:
        factorial = factorial*n
        n -= 1
    return factorial

rec_size = sys.getsizeof(Recursion(n)) #знаходимо розмір обох функцій
iter_size = sys.getsizeof(Iteration(n))

if i == '1':
    print(f'{b}! = {Recursion(n)}')
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # знаходимо час викрнання функцій
    print(f'The amount of occupied memory - {rec_size}')
    print(f'The program lasted {t} seconds')
else:
    print(f'{b}! = {Iteration(n)}')
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f'The amount of occupied memory - {iter_size}')
    print(f'The program lasted {t} seconds')
