from gempa import *
lokasi1 = gempa('Banten',1.2)
lokasi2 = gempa('Palu',6.1)
lokasi3 = gempa('Cianjur',5.6)
lokasi4 = gempa('Jayapura',3.3)
lokasi5 = gempa('Garut',4)

print('info Gempa terkini')
print()
lokasi1.hitungdampak()
lokasi2.hitungdampak()
lokasi3.hitungdampak()
lokasi4.hitungdampak()
lokasi5.hitungdampak()