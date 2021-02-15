#buatlah sebuah program untuk mencari tahu apakah
#seseorang bisa mendapatkan sim setelah mengikuti test
#dengan standar umur harus diatas 17 tahun 
#dan nilai test harus lebih dari 60!

#Input umur dan nilai test yang kita ikuti

#proses mengecek apakah umur dan nilai kita cukup untuk mendapatkan sim

#Output apakah kita lulus dan berhak untuk mendapatkan sim atau tidak 

umur = int(input("Masukan umur anda :"))
nilai = int(input("Masukan nilai test anda :"))
lulus = ("Selamat anda berhak mendapatkan SIM")
gagalUmur = ("Maaf umur anda belum mencukupi untuk mendapatkan SIM\nSilahkan coba lagi bulan atau tahun depan")
gagalNilai = ("Maaf nilai anda tidak mencukupi untuk mendapatkan SIM\nSilahkan coba lagi bulan atau tahun depan")

if (umur>17):
    print()
    if (nilai>60):
        print()
        print (lulus)
    else:
        print ()
        print(gagalNilai)
else :
    print()
    print(gagalUmur)