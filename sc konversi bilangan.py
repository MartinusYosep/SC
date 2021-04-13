#Buatlah sebuah kalkulator untuk mengkonversi 
#bilangan desimal ke bilangan biner, octal dan hexadesimal

#input : nilai desimal
#proses : dikonversi menjadi bilangan biner,octal atau hexadesimal
#output : nilai desimal yg telah dikonversi menjadi biner , octal atau hexadesimal

print("Kalkulator Konversi")
print("===================")
print("1.Biner\n2.Octal\n3.Hexadesimal")
O = int(input("Masukkan pilihan anda :"))
if O == 1 :
    desimal = int(input("Masukkan angka :"))
    biner = bin(desimal).replace("0b",'')
    print(biner)
elif O == 2 :
    desimal = int(input("Masukkan angka :"))
    octal = oct(desimal).replace("0o","")
    print(octal)
elif O == 3 :
    desimal = int(input("Masukkan angka :"))
    hexa = hex(desimal).replace("0x",'')
    print(hexa.upper())
else :
    print("Maaf pilihan anda tidak tersedia, coba cek lagi!")