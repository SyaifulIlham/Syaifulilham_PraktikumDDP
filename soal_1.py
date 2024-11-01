listVariabelKendaraan = ["Skyline GTR R34", "Mobil", 4200, "Biru", 4]

# - Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
harga_kendaraan = 800000000 
tipe_kendaraan = "Sport Car"
merk_kendaraan = "Nissan"

# - Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
print("Tugas Nomer : 1")

print("- Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan] : -> Hasil Dibawah :")
listVariabelKendaraan.append(harga_kendaraan)
listVariabelKendaraan.append(tipe_kendaraan)
listVariabelKendaraan.insert(2,merk_kendaraan)
print(listVariabelKendaraan)