from hitung import*

def hitungan_bangun_datar():
 print("\n pilih hitung luas")
 print("1.luas segitiga")
 print("2.luas persegi")
 print("3.luas persegi panjang")
 print("4.luas lingkaran")
 print("5.luas belah ketupat")
 
 pilihan = int(input("\n masukan pilihan 1 - 5 : "))
 
 if pilihan == 1:
     a = float(input("masukan alas : "))
     t = float(input("masukan tinggi : "))
     print("hasil luas segitiga : ", segitiga(a,t))
     
 elif pilihan == 2:
     s = float(input("masukan sisi : "))
     print("hasil luas persegi : ", persegi(s))
     
 elif pilihan == 3:
     p = float(input("masukan panjang : "))
     l = float(input("masukan lebar : "))
     print("hasil luas persegi panjang : ", persegi_panjang(p,l))
     
 elif pilihan == 4:
     r = float(input("masukan jari - jari : "))
     print("hasil luas lingkaran : ", lingkaran(r))
     
 elif pilihan == 5:
     d1 = float(input("masukan diagonal 1 : "))
     d2 = float(input("masukan diagonal 2 : "))
     print("hasil luas belah ketupat : ", belah_ketupat(d1,d2))
 else:
     print("pilihan tidak valid")

hitungan_bangun_datar()
    