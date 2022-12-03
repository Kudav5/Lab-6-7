# Tugas Praktikum
'''
buat program dengan  menampilkan daftar nilai mahasiswa dengan ketentuan:
tambah()
tampilkan()
hapus(nama)
ubah(nama)
'''
def tambah(x,y):
    return x+y
def tampilkan(x,y):
    return x,y
def hapus(nama, nilai):
    return
def ubah(nama):
    return
# buat flowcart serta penjelasan

print(tambah(2,1))
#===================================================================


print("Program Daftar Nilai")
print("====================")
print()

while True:
    a = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] :")
    if a=='T':
        print('Tambah Data')