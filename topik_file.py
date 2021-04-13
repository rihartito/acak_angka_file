
''' buat sebuah program ramalan yang dimana angkanya dari 1 sampai 5 akan diacak setiap nomor
berisi sebuah ramalan buat hari ini,hasilnya akan ditaruh di file yang telah disediakan yaitu ramalan.txt


input:nama = mengisikan nama user

proses:
open file ramalan
import random 
melakukan percabangan di setiap angka
write file hasilnya
close file

output:
menampilkan hasil ramalan di file ramalan

'''
masuk = open("ramalan.txt","w")
import random
angka_bulat = random.randint(1,5)
print("====Ramalan hari ini====")
nama = input("masukkan nama:")

if angka_bulat == 1:
    masuk.write("====Ramalan hari ini===="+"\n")
    masuk.write(nama + " nomor ramalannya adalah "+ str(angka_bulat)+ " : yang berarti hari ini anda memliki keberuntungan")
    print(angka_bulat)
elif angka_bulat == 2 :
    masuk.write("====Ramalan hari ini===="+"\n")
    masuk.write(nama + " nomor ramalannya adalah "+ str(angka_bulat)+ " : yang berarti hari ini anda akan mendapatkan suatu masalah yang gampang")
    print(angka_bulat)
elif angka_bulat == 3 :
    masuk.write("====Ramalan hari ini===="+"\n")
    masuk.write(nama + " nomor ramalannya adalah "+ str(angka_bulat)+ " : yang berarti hari ini sama seperti kemarin")
    print(angka_bulat)
elif angka_bulat == 4 :
    masuk.write("====Ramalan hari ini===="+"\n")
    masuk.write(nama + " nomor ramalannya adalah "+ str(angka_bulat)+ " : yang berarti hari ini adalah hari yang buruk")
    print(angka_bulat)
else :
    masuk.write("====Ramalan hari ini===="+"\n")
    masuk.write(nama + " nomor ramalannya adalah "+ str(angka_bulat)+ " : yang berarti hari ini kesialan akan menimpa anda")
    print(angka_bulat)
masuk.close()
