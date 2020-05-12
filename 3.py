'''
Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Постолович А.С. 122-В
'''
import random
import sys
import timeit

n = int(input("Choose size of matrix from 1 to 5: "))
while 1>=n>=5:
    n = int(input("Input num from 1 to 5: "))


A = []
for i in range(n):
    a = [random.randint(-100,100) for k in range(n)]
    A.append(a)
for i in range(n):
    print(A[i])


def Iteration(A):
    max = A[0][0]
    c,d = 0,0
    for i in range(n):
        for j in range(n):
            if max < A[i][j]:
                max = A[i][j]
                c, d = i,j
    print(f'A[{c}][{d}] is max element in matrix')

iter_size = sys.getsizeof(Iteration(A))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

print(f'The program lasted {t} seconds')
print(f'The amount of occupied memory - {iter_size}')

'''
Мені не вдалося написати функцію для знаходження найбільшого елемента методом рекурсії
тому залишив як єю.
'''