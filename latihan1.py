import random

def random_num(n):
  numbers = []
  for i in range(n):
    number = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    while number >= 0.5:  # Ulangi hingga mendapatkan bilangan yang lebih kecil dari 0.5
      number = random.random()
    numbers.append(number)
  return numbers
# Meminta input dari pengguna untuk jumlah bilangan acak
n = int(input("Masukkan nilai N: "))
# Menghasilkan bilangan acak
random_numbers = random_num(n)
# Menampilkan bilangan acak
for i, number in enumerate(random_numbers):
  print(f"data ke: {i+1} => {number}")
print("Selesai")