import random

N = int(input("Masukkan nilai N: "))

for i in range(1, N + 1):
  angka_acak = random.random()  # Menghasilkan angka acak antara 0 dan 1
  while angka_acak >= 0.5:  # Ulangi hingga angka_acak < 0.5
    angka_acak = random.random()
  print(f"data ke: {i} => {angka_acak}")

print("Selesai")