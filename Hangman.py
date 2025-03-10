import random  # Mengimpor modul random untuk memilih kata secara acak

# Daftar kata yang bisa ditebak
words = ["CHICKEN", "COW", "SHEEP", "DEER", "ELEPHANT", "ARMADILLO"]

# Memilih kata secara acak dari daftar words
random_word = random.choice(words)

# Membuat daftar berisi karakter "_" sebanyak panjang kata yang dipilih
guessed_word = ["_"] * len(random_word)

# Mengubah kata menjadi list agar bisa dicocokkan dengan tebakan pengguna
blanks = list(random_word)

# Menentukan jumlah percobaan yang diperbolehkan
attempts = 6

# Menyimpan huruf yang sudah ditebak agar tidak ditebak ulang
guessed_letters = set()

# Loop utama permainan, berjalan selama masih ada "_" dalam guessed_word dan percobaan masih tersedia
while attempts > 0 and "_" in guessed_word:
    print("\n" + " ".join(guessed_word))  # Menampilkan kata dengan huruf yang sudah ditebak
    guessed = input("Guess a letter: ").upper()  # Meminta input huruf dari pengguna dan mengubahnya menjadi huruf besar

    # Validasi input: harus satu huruf dan berupa alfabet
    if len(guessed) != 1 or not guessed.isalpha():
        print("Masukkan satu huruf!")
        continue

    # Cek apakah huruf sudah pernah ditebak sebelumnya
    if guessed in guessed_letters:
        print("Kamu sudah menebak huruf ini!")
        continue

    # Menambahkan huruf yang ditebak ke dalam set guessed_letters
    guessed_letters.add(guessed)

    # Jika huruf ada dalam kata yang dipilih
    if guessed in blanks:
        # Mengganti "_" dengan huruf yang benar di posisi yang sesuai
        for i in range(len(random_word)):
            if blanks[i] == guessed:
                guessed_word[i] = guessed
        print("Benar!")
    else:
        # Mengurangi jumlah percobaan jika tebakan salah
        attempts -= 1
        print(f"Salah! Sisa percobaan: {attempts}")

# Mengecek apakah kata telah berhasil ditebak atau tidak
if "_" not in guessed_word:
    print("\nSelamat! Kamu berhasil menebak kata:", random_word)
else:
    print("\nKamu kalah! Kata yang benar adalah:", random_word)
