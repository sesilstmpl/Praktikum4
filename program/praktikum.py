nilai = []
perulangan = True
while perulangan:
    nama = input("Masukkan Nama Mahasiswa   : ")
    nim = input("Masukkan NIM              : ")
    tugas = int(input("Masukkan Nilai Tugas      : "))
    uts = int(input("Masukkan Nilai UTS        : "))
    uas = int(input("Masukkan Nilai UAS        : "))
    akhir =(tugas * 30/100) + (uts * 35/100) + (uas * 35/100)

    nilai.append([nama,nim,tugas,uts,uas,int(akhir)])
    if(input("Tambah Data (y/t)? ") =='t'):
        perulangan=False
print("---------------------------------------------------------------------------------")
print("\n                               DAFTAR NILAI MAHASISWA                    ")
print("---------------------------------------------------------------------------------")
print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
print("---------------------------------------------------------------------------------")
i = 0                                                                         
for item in nilai:                                                             
    i += 1
    print("| {no:2d} | {nama:14s} | {nim:11s} | {tugas:7d} | {uts:7d} | {uas:7d} | {akhir:7f}   |"
         .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
print("---------------------------------------------------------------------------------")