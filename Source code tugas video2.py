#Buatlah segitiga bintang menggunakan perintah perulangan

#Input = jumlah dari baris bintang yang akan kita buat, "*"*(1+2*i).center(1+x*X)
#Proses = program akan menyusun segitiga yang akan kita buat menggunakan perintah perulangan
#Output = Menampilkan segitiga yang telah kita masukkan rumus dan jumlah barisnya

X = int(input("Masukkan Jumlah baris :"))

for i in range (X):
    print(("*"*(1+2*i)).center(1+X*X))
