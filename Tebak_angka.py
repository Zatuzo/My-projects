import random

# Memilih angka acak antara 1 dan 100
angka_benar = random.choice(range(1, 101))  # 101 agar mencakup angka 100

# Pengguna diberikan 5 kesempatan untuk menebak
for i in range(5):
    try:
        # Meminta input dari pengguna
        Angka_tebakan = int(input("Masukkan angka antara 1-100: "))

        # Periksa apakah angka dalam rentang yang valid
        if Angka_tebakan < 1 or Angka_tebakan > 100:
            print("Nilainya di luar angka tebakan! Masukkan angka antara 1-100.")
            continue  # Melanjutkan ke iterasi berikutnya tanpa menghitung percobaan

        # Cek apakah tebakan terlalu rendah
        if Angka_tebakan < angka_benar:
            print("Terlalu rendah nilainya!")
        # Cek apakah tebakan terlalu tinggi
        elif Angka_tebakan > angka_benar:
            print("Terlalu tinggi nilainya!")
        # Jika benar, cetak hasil dan hentikan permainan
        else:
            print(f"Selamat! Anda menebak dengan benar: {angka_benar}")
            break
    except ValueError:
        print("Harap masukkan angka yang valid!")  # Menangani input non-angka
else:
    print(f"Maaf, kesempatan Anda habis. Angka yang benar adalah {angka_benar}.")
