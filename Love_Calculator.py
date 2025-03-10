def calculate_love_score(name1, name2):
    # Ubah kedua nama menjadi huruf besar agar perhitungan tidak case-sensitive
    name1 = name1.upper()
    name2 = name2.upper()  

    # Inisialisasi variabel untuk menghitung jumlah kemunculan huruf dalam "TRUE LOVE"
    T, R, U, E, L, O, V = 0, 0, 0, 0, 0, 0, 0

    # Menghitung jumlah masing-masing huruf dalam kedua nama
    T += name1.count("T") + name2.count("T")
    R += name1.count("R") + name2.count("R")
    U += name1.count("U") + name2.count("U")
    E += name1.count("E") + name2.count("E")
    L += name1.count("L") + name2.count("L")
    O += name1.count("O") + name2.count("O")
    V += name1.count("V") + name2.count("V")

    # Menghitung total nilai berdasarkan aturan:
    # - Jumlah huruf dalam "TRUE" dikalikan 10 (puluhan)
    # - Jumlah huruf dalam "LOVE" sebagai satuan
    total1 = (T + R + U + E) * 10
    total2 = L + O + V + E

    # Mengembalikan hasil perhitungan
    return total1 + total2

# Meminta input dari pengguna, di mana nama pertama dan kedua harus dipisahkan dengan spasi
name1, name2 = input("").split()

# Memanggil fungsi dan mencetak hasil skor cinta
print(calculate_love_score(name1, name2))
