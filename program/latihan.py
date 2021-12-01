# Akses list

## List sebanyak 5 elemen 
list = [1,2,3,4,5]
print("Membuat list yang berisi 5 elemen")
print(list)

## Tampilkam elemen ke 3
print("Menampilkan elemen ketiga pada list tersebut")
print(list[-3])
print(list[2])

## Ambil nilai elemen ke 2 sampai elemen ke 4
print("Ambil nilai elemen ke 2 sampai elemen ke 4")
print(list[1:4])

## Ambil elemen terakhir
print("Ambil elemen terakhir")
print(list[-1])

# Ubah Elemen List

## Ubah elemen ke 4 dengan nilai lainnya
print("Ubah elemen ke 4 dengan nilai lainnya")
odd = [1,2,3,4,5]
odd[3] = 10
print(odd)

## Ubah elemen ke 4 sampai dengan elemen terakhir
print("Ubah elemen ke 4 sampai dengan elemen terakhir")
odd[3:5] = [10,11]
print(odd)

# Tambah Elemen List

## Ambil 2 bagian dari list pertama (A) dan jadikan list Ke-2 (B)
print("Ambil 2 bagian dari list pertama (A) dan jadikan list Ke-2 (B)")
A = [1,2,3,4,5]
B = A[1:3]
print(B)

## Tambah list B dengan Nilai String
print("Tambah list B dengan Nilai String")
B.append("Sesil")
print(B)

## Tambah List B dengan 3 nilai
print("Tambah List B dengan 3 nilai")
print(B + [7,8])

## Gabungkan list B dan List A
print("Gabungkan list B dan List A")
print(B + A)