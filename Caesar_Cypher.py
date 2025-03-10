# Daftar huruf alfabet dalam urutan yang tetap
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(original_text, shift_amount):
    """Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher."""
    cipher_text = ""  # Variabel untuk menyimpan teks hasil enkripsi
    
    for letter in original_text:  # Iterasi setiap huruf dalam teks asli
        if letter in alphabet:  # Hanya mengenkripsi jika huruf ada dalam alfabet
            shifted = (alphabet.index(letter) + shift_amount) % 26  
            # Menentukan indeks baru dengan pergeseran, lalu mengambil modulus 26 agar tetap dalam alfabet
            cipher_text += alphabet[shifted]  # Menambahkan huruf yang telah dienkripsi ke cipher_text
        else:
            cipher_text += letter  # Jika bukan huruf alfabet, langsung tambahkan tanpa perubahan
            
    return cipher_text  # Mengembalikan teks yang telah dienkripsi

def decode(cipher_text, shift_amount):
    """Fungsi untuk mendekripsi teks yang telah dienkripsi menggunakan Caesar Cipher."""
    normal_text = ""  # Variabel untuk menyimpan hasil dekripsi
    
    for letter in cipher_text:  # Iterasi setiap huruf dalam teks terenkripsi
        if letter in alphabet:  # Hanya mendekripsi jika huruf ada dalam alfabet
            original = (alphabet.index(letter) - shift_amount) % 26  
            # Menentukan indeks asli sebelum enkripsi dengan mengurangkan shift
            normal_text += alphabet[original]  # Menambahkan huruf yang telah didekripsi ke normal_text
        else:
            normal_text += letter  # Jika bukan huruf alfabet, langsung tambahkan tanpa perubahan
            
    return normal_text  # Mengembalikan teks yang telah didekripsi

# Meminta pengguna untuk memilih antara enkripsi atau dekripsi
print("Do you want to encrypt or decode?")
choice = input().strip().upper()  # Menghapus spasi tambahan dan mengubah input ke huruf besar

if choice == "ENCRYPT":  
    # Jika pengguna memilih enkripsi
    original_text = input("Enter text to encrypt: ").strip().upper()  
    # Meminta input teks asli dan mengubahnya menjadi huruf besar
    shift_amount = int(input("Enter shift amount: ").strip())  
    # Meminta input angka pergeseran (shift) dalam bentuk integer
    print("Encrypted text:", encrypt(original_text, shift_amount))  
    # Menampilkan hasil enkripsi

elif choice == "DECODE":  
    # Jika pengguna memilih dekripsi
    cipher_text = input("Enter text to decode: ").strip().upper()  
    # Meminta input teks terenkripsi dan mengubahnya menjadi huruf besar
    shift_amount = int(input("Enter shift amount: ").strip())  
    # Meminta input angka pergeseran (shift) dalam bentuk integer
    print("Decrypted text:", decode(cipher_text, shift_amount))  
    # Menampilkan hasil dekripsi

else:
    print("Invalid choice! Please enter 'ENCRYPT' or 'DECODE'.")  
    # Jika pengguna memasukkan input yang tidak valid
