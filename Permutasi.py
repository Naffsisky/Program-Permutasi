      # Nama  : Prinafsika
      # NIM   : 21081010278
#module 
from itertools import permutations
import pyfiglet 

intro = pyfiglet.figlet_format("Permutasi", font = "standard")
intronama = pyfiglet.figlet_format('By : Naff', font = "slant")

#user input + penghitungan
print(intro)
print(intronama)
print('|--------------------------------------|')
print('| Rumus permutasi adalah : n! / (n-r)! |')
print('|--------------------------------------|')

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
a = n
b = r

#penghitungan n
faktorial = 1

while a>=1 :
      print (a, end = '.')
      a = a-1

for i in range(1, n + 1):
  faktorial *= i

print(f' | {n}! = {faktorial}')

#penghitungan r
faktorial = 1

while b>=1 :
      print (b, end = '.')
      b = b-1

for j in range(1, r + 1):
  faktorial *= j

print(f' | {r}! = {faktorial}')

#output
print('------------------------- :')
print("         ",hasil)
print('Hasil permutasinya adalah :', hasil)
