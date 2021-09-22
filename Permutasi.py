from itertools import permutations 

print('Rumus permutasi adalah : n! / (n-r)!')
n = int(input('Masukkan angka untuk n : '))
r = int(input('Masukkan angka untuk r : '))
def faktorial(x):
               if x == 1:
                   return 1
               elif x == 0:
                   return 1
               else:
                   return (x*faktorial(x-1))
hasil = (faktorial(n)/faktorial(n-r))

faktorial = 1

for i in range(1, n + 1):
  faktorial *= i

print(f'{n}! = {faktorial}')

faktorial = 1

for j in range(1, r + 1):
  faktorial *= j

print(f'{r}! = {faktorial}')

print('------------- :')
print(hasil)
print('Hasil permutasinya adalah :', hasil)