#Buatlah sebuah kalkulator untuk menghitung :
#1. faktorial dari suatu bilangan n.
#2. akar kubik dari suatu bilangan n.
#3. sisa hasil bagi dari suatu bilangan n, dibagi dengan bilangan x
#buat kalkulator ini dengan template fungsi dibawah ini :

#def faktorial(n):
#…rumus faktorial [n * faktorial(n-1)]

#def akarKubik(n):
#…rumus akar kubik [n ** (1/3)]

#def sisaHasilBagi(n,x):
#… rumus [n % x]

#input    : nilai yang ingin kita hitung, rumus faktorial, akar kubik, dan sisa hasil bagi
#proses   : mencari nilai yang ingin dihitung 
# #output : hasil dari apa ingin kita hitung 

print("======= Kalkulator advance =======")
print ("Pilih menu untuk melakukan perhitungan advance :")
print("1. Faktorial\n2.Akar kubik\n3. Sisa hasil bagi")
O = int(input("Masukkan pilihan anda :"))
if O == 1 :
    n = int(input("Masukkan angka yang ingin dihitung faktorialnya :"))
    def faktorial(n):
        if n == 1:
            return 1
        else :
            return n * faktorial(n-1)
    print(n,"Faktorialnya adalah :",faktorial(n))
elif O == 2 : 
    n = int(input("Masukkan angka yang ingin dihitung akar kubiknya :"))
    def akarKubik(n):
        if n == 1:
            return 1 
        else :
            return n ** (1/3)
    print("Akar kubik dari",n,"adalah",akarKubik(n))
elif O == 3 :
    n = int(input("Masukkan angka yang ingin dibagi :"))
    x = int( input("Masukkan pembagi :"))
    def sisaHasilBagi(n,x):
        if (n,x) == 1:
            return 1
        else:
            return n % x
    print ("Sisa hasil bagi dari",n,"dengan",x,'adalah',sisaHasilBagi(n,x))
else:
    print("Maaf pilihan anda tidak tersedia. Silahkan buat kalkulator anda sendiri.")
    