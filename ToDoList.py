# Inisialisasi list kosong untuk menyimpan daftar aktivitas
daftar = []

# Fungsi untuk menampilkan menu utama
def menu():
    print("\n1. Tambah aktifitas")  # Opsi untuk menambah aktivitas ke daftar
    print("2. Hapus aktifitas")  # Opsi untuk menghapus aktivitas dari daftar
    print("3. Tunjukkan aktifitas yang sudah ada")  # Opsi untuk menampilkan daftar aktivitas
    print("4. Keluar dari Menu")  # Opsi untuk keluar dari program

# Fungsi untuk menampilkan daftar aktivitas yang tersimpan
def Tunjukkan_daftar():
    if len(daftar) > 0:  # Mengecek apakah daftar berisi aktivitas atau kosong
        print("\nIsi List kamu:")
        # Loop untuk menampilkan semua aktivitas dalam daftar dengan nomor indeks
        for index, aktifitas in enumerate(daftar):
            print(f"{index}. {aktifitas}")
    else:
        print("\nList kamu kosong!")  # Jika daftar kosong, beri tahu pengguna

# Fungsi untuk menambahkan aktivitas ke dalam daftar
def Tambah_list():
    aktifitas = input("Masukkan aktifitas yang ingin dimasukkan: ")  # Meminta input dari pengguna
    daftar.append(aktifitas)  # Menambahkan aktivitas ke dalam daftar
    print(f"Aktivitas '{aktifitas}' telah dimasukkan ke dalam daftar!")  # Konfirmasi ke pengguna

# Fungsi untuk menghapus aktivitas dari daftar berdasarkan nomor indeks
def Hapus_daftar():
    if len(daftar) == 0:  # Mengecek apakah daftar kosong sebelum menghapus
        print("\nList kamu kosong! Tidak ada yang bisa dihapus.")
        return  # Keluar dari fungsi jika tidak ada aktivitas yang bisa dihapus

    Tunjukkan_daftar()  # Menampilkan daftar agar pengguna bisa memilih nomor yang ingin dihapus
    
    try:
        Hapus = int(input("Pilih Nomor aktifitas yang ingin dihapus: "))  # Meminta nomor indeks dari pengguna
        daftar_terhapus = daftar.pop(Hapus)  # Menghapus aktivitas berdasarkan indeks yang dipilih
        print(f"Aktivitas '{daftar_terhapus}' telah dihapus!")  # Konfirmasi ke pengguna
    except (IndexError, ValueError):  # Menangani error jika input bukan angka atau indeks tidak valid
        print("Nomor yang dimasukkan tidak valid.")  # Pesan kesalahan jika input salah

# Loop utama program
while True:
    menu()  # Menampilkan menu utama
    pilihan = input("Pilihlah Hal yang ingin dilakukan: ")  # Meminta input pilihan dari pengguna

    if pilihan == "1":  # Jika pengguna memilih opsi 1, jalankan fungsi Tambah_list()
        Tambah_list()
    elif pilihan == "2":  # Jika pengguna memilih opsi 2, jalankan fungsi Hapus_daftar()
        Hapus_daftar()
    elif pilihan == "3":  # Jika pengguna memilih opsi 3, jalankan fungsi Tunjukkan_daftar()
        Tunjukkan_daftar()
    elif pilihan == "4":  # Jika pengguna memilih opsi 4, keluar dari program
        print("Telah keluar dari program daftar.")
        break  # Menghentikan loop, sehingga program berhenti
    else:
        print("Pilihan tidak sesuai. Silakan coba lagi!")  # Jika input tidak valid, minta input ulang
