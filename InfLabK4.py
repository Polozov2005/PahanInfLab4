import numpy as np
import random

## Генерация случайной матрицы смежностей A
# Генерация случайного натурального числа v
v = random.randint(1, 12)

# Генерация случайного натурального числа r
r = random.randint(0, 24)
print('v =', v)
print('r =', r)

# Генерация пустой матрицы A размером v*v
A = np.zeros((v, v), dtype=np.int64)
# Объявление счётчика n
n = 0

while n != r:
    # Гененерация случайного натурального числа i
    i = random.randint(0, v-1)

    # Гененерация случайного натурального числа j
    j = random.randint(0, v-1)

    A[i, j] += 1
    A[j, i] += 1
    n += 1

print(A)

## Определение степеней всех нечётных вершин
# Объявление множества степеней S
S = []

print('(Отсчёт вершин начинается с 0)')
for i in range(v):
    s = 0
    for j in range(v):
        s += A[i, j]
    S.append(s)
    print('Степень вершины', i, 'равна', S[i])

## Определение числа компонент связности
# Объявление списка компонент связности K
K = [[0]]

# Объявление счётчика компонент k
k = 0

# Объявление списка посещённых вершин visited_nodes
visited_nodes = [0]

# Объявление счётчика посещённых вершин n
n = 0

while n != v:
    # Объявление счётчика порядкового номера вершины в k-ой компоненте a
    a = 0
    while a != len(K[k]):
        i = K[k][a]
        for j in range(v):
            if not(j in visited_nodes) and A[i, j] > 0:
                K[k] += [j]
                visited_nodes += [j]
                n += 1
        a += 1
    i = 0
    while i in visited_nodes:
        i += 1
    visited_nodes += [i]
    n += 1
    K += [[i]]
    k += 1
K.pop()
print('Число компонент равно', len(K))

## Преобразование матрицы смежности к списку инцидентности
# Объявление списка инцидентности
INCIDENCE = []
A_copy = np.copy(A)
for i in range(A.shape[0]):
    for j in range(i, A.shape[0]):        
        while A_copy[i, j] != 0:
            INCIDENCE.append([i, j])
            A_copy[i, j] += -1

print('Список инциденций')
print(INCIDENCE)