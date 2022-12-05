# Tugas Praktikum

data = {}
def tambah(nama, nilai):                # untuk menambah data
    a = data[nama] = nilai
def tampilkan(a):                       # untuk menampilkan data
    return data
def hapus(nama):                        # untuk menghapus data berdasarkan nama
    print('menghapus data', nama)
    if nama in data.keys():
        del data[nama]
    return nama, 'sudah dihapus'
def ubah(nama):                         # untuk mengubah data berdasarkan nama
    print('mengubah data ', nama)
    if data.keys():
        del data[nama]
        nama = input("Nama baru: ")
        nilai = input('Nilai baru: ')
    data[nama] = nilai

print('Menambah data')
print(tambah('Davin', 18))
print(tambah('Ariel', 20))
print(tambah('Dani', None))
print()

print('menampilkan data')
print(tampilkan(data))
print()

print(ubah('Ariel'))
print()

print(hapus('Dani'))
print()

print('menampilkan data lagi')
print(tampilkan(data))