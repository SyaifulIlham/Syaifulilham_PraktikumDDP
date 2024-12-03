from hitung import*

def hitungan_aritmatika():
 print("\n pilih operasi hitung")
 print("1.penambahan")
 print("2.pengurangan")
 print("3.perkalian")
 print("4.pembagian")
 print("5.Pangkat")
 
 pilihan = int(input("\n masukan angka 1 - 5 : "))
 
 if pilihan == 1:
     a = float(input("masukan angka pertama : "))
     b = float(input("masukan angka kedua : "))
     print("hasil penambahan:", tambah(a,b))
 elif pilihan == 2:
     a = float(input("masukan angka pertama : "))
     b = float(input("masukan angka kedua : "))
     print("hasil pengurangan:", kurang(a,b))
 elif pilihan == 3:
     a = float(input("masukan angka pertama : "))
     b = float(input("masukan angka kedua : "))
     print("hasil perkalian:", kali(a,b))
 elif pilihan == 4:
     a = float(input("masukan angka pertama : "))
     b = float(input("masukan angka kedua : "))
     print("hasil pembagian:", bagi(a,b))
 elif pilihan == 5:
     a = float(input("masukan angka pertama : "))
     b = float(input("masukan angka kedua : "))
     print("hasil pangkat:", pangkat(a,b))
 else:
     print("pilihan tidak valid")

hitungan_aritmatika()
    