# Mengimpor modul 'random' untuk menghasilkan karakter secara acak
import random

# List huruf besar dan kecil
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List angka 0-9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List simbol yang umum digunakan dalam password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Menampilkan pesan pembuka
print("Welcome to the PyPassword Generator!")

# Meminta input jumlah huruf, simbol, dan angka dari pengguna
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Membuat password dalam mode "Easy" (tanpa diacak urutannya)
# Contoh: 4 huruf, 2 simbol, 2 angka = JduE&!91
password = ""

# Menambahkan huruf secara acak sesuai jumlah yang diminta pengguna
for i in range(nr_letters):
    password += random.choice(letters)

# Menambahkan simbol secara acak sesuai jumlah yang diminta pengguna
for i in range(nr_symbols):
    password += random.choice(symbols)

# Menambahkan angka secara acak sesuai jumlah yang diminta pengguna
for i in range(nr_numbers):
    password += random.choice(numbers)

# Menampilkan password dalam mode "Easy" (tanpa pengacakan karakter)
print("Easy:", password)

# Mode "Hard" - Password dengan karakter yang diacak urutannya
# Contoh: 4 huruf, 2 simbol, 2 angka = g^2jk8&P

# Mengubah string 'password' menjadi list agar bisa diacak
Hard = list(password)

# Mengacak isi list
random.shuffle(Hard)

# Menggabungkan kembali list menjadi string
password = "".join(Hard)

# Menampilkan password dalam mode "Hard" (dengan karakter diacak)
print("Hard:", password)
