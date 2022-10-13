import random
razm1 = int(input("Введите размерность первого массива: "))
razm2 = int(input("Введите размерность второго массива: "))
list1 = [random.randint(0, 50) for i in range(razm1+1)]
list2 = [random.randint(0, 50) for j in range(razm2+1)]
c = list(set(list1) & (set(list2)))
if len(c) == 0:
    print("Одинаковых элементов нет, попробуйте ещё раз")
else:
    print("В обоих массивах встречаются такие элементы, как:", c)

# print(list1)
# print(list2)
