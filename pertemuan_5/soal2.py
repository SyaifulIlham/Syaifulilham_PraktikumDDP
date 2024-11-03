print("""
      pilih 1 untuk mencari luas persegi
      pilih 2 untuk mencari luas lingkaran
      pilih 3 untuk mencari luas segitiga
      """)
pilih_rumus = int(input("pilih nomor rumus : "))

match pilih_rumus:
    case 1 :
        sisi = int(input("masukan sisi(cm) : "))
        luas_persegi = sisi * sisi
        print("hasil hitung luas persegi =", luas_persegi)
    case 2 :
        phi = 3.14
        rusuk = int(input('masukan rusuk lingkaran(cm) : '))
        luas_lingkaran = phi * rusuk**2
        print("hasil hitung luas lingkaran =",luas_lingkaran)
    case 3 :
        alas = int(input("masukan alas(cm) : "))
        tinggi = int(input("masukan tinggi(cm) : "))
        luas_segitiga = 0.5 * alas * tinggi
        print("hasil hitung luas segitiga =",int(luas_segitiga),"Cm")
    case _:
        print("tidak memasukan input / input salah")