razm = int(input("Введите разменость массива: "))
Massiv = [0]*razm
k = 0
for i in Massiv:
    k += 1
    print('Введите элемент массива №', k)
    Massiv[k-1] = float(input('Ввод: '))
maxindex = Massiv.index(max(Massiv))
for j in range(maxindex+1, k):
    Massiv[j] = 0
print(Massiv)
