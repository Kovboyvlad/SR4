razm = int(input("Введите разменость массива: "))
delta = int(input("Введите дельту: "))
Massiv = [0]*razm
q, k = 0, 0
minimal = 0
for i in Massiv:
    k += 1
    print('Введите элемент массива №', k)
    Massiv[k-1] = int(input('Ввод: '))

minimal = min(Massiv)
for j in Massiv:
    if j - delta == minimal:
        q += 1
print(q)