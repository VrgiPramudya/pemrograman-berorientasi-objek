#1. Number (int, float, complex)
#Integer (int)
angka_int = 10
print("angka_int =", angka_int, "->", type(angka_int))

#Float
angka_float = 3.14
print("angka_float =", angka_float, "->", type(angka_float))

#Complex
angka_complex = 2 + 3j
print("angka_complex =", angka_complex, "->", type(angka_complex))

#2. Boolean
is_active = True
print("is_active =", is_active, "->", type(is_active))

#3. String
teks = "Hello, Python!"
print("teks =", teks, "->", type(teks))

#4. List
#List adalah tipe data terurut dan dapat diubah (mutable)
daftar_angka = [1, 2, 3, 4, 5]
print("daftar_angka =", daftar_angka, "->", type(daftar_angka))

#5. Tuple
# Tuple adalah tipe data terurut tetapi tidak dapat diubah (immutable)
koordinat = (10, 20)
print("koordinat =", koordinat, "->", type(koordinat))

#6. Dictionary
#Dictionary menyimpan data dalam pasangan key-value
data_mahasiswa = {
    "nama": "Andi",
    "nim": "A11.2022.12345",
    "jurusan": "Teknik Informatika"
}
print("data_mahasiswa =", data_mahasiswa, "->", type(data_mahasiswa))

#7. Set
#Set adalah tipe data yang tidak terurut, unik (tiap elemen hanya muncul 1x)
himpunan_angka = {1, 2, 3, 2, 1}
print("himpunan_angka =", himpunan_angka, "->", type(himpunan_angka))

#8. Contoh penggunaan konversi tipe data
nilai_str = "100"
print("\nnilai_str =", nilai_str, "->", type(nilai_str))

nilai_int = int(nilai_str) # konversi string ke integer
print("nilai_int =", nilai_int, "->", type(nilai_int))