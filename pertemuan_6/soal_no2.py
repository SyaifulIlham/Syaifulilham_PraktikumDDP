angka = 0
for num in range(1,20,2):
    angka += num
    print(num,end=" + " if num < 19 else " = ")

print(angka)
    