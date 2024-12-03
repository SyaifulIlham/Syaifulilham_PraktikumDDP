from hitung import*

def hitungan_bangun_ruang():
 print("\n pilih hitung luas permukaan bangun ruang")
 print("1.luas permukaan balok")
 print("2.luas permukaan kubus")
 print("3.luas permukaan tabung")
 print("4.luas permukaan kerucut")
 print("5.luas permukaan limas")
 
 pilihan = int(input("\n masukan pilihan 1 - 5 : "))
 
 if pilihan == 1:
     p = float(input("masukan panjang : "))
     l = float(input("masukan lebar : "))
     t = float(input("masukan tinggi : "))
     print("hasil luas permukaan balok : ", luas_permukaan_balok(p,l,t))
     
 elif pilihan == 2:
     s = float(input("masukan sisi : "))
     print("hasil luas permukaan kubus : ", kubus(s))
     
 elif pilihan == 3:
     r = float(input("masukan jari - jari : "))
     t = float(input("masukan tinggi : "))
     print("hasil luas permukaan kubus panjang : ", tabung(r,t))
     
 elif pilihan == 4:
     r = float(input("masukan jari - jari : "))
     t = float(input("masukan tinggi : "))
     print("hasil luas permukaan kerucut : ", kerucut(r))
     
 elif pilihan == 5:
     s = float(input("masukan Panjang sisi alas : "))
     t_s = float(input("masukan tinggi sisi tegak : "))
     print("hasil luas permukaan limas : ", luas_permukaan_limas(s,t_s))
 else:
     print("pilihan tidak valid")

hitungan_bangun_ruang()
    