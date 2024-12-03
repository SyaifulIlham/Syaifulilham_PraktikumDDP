import math

def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b
 
def bagi(a,b):
    if b == 0:
        return "Error: pembagian oleh nol tidak boleh"
    else:
        return a/b

def pangkat(a,b):
    return math.pow(a,b)

#bangun datar
def segitiga(a,t):
    return 0.5 * a * t

def persegi(s):
    return s * s

def persegi_panjang(p,l):
    return p * l

def lingkaran(r):
    return math.pi * (r ** 2)

def belah_ketupat(d1,d2):
    return 0.5 * d1 * d2

def luas_permukaan_balok(p,l,t):
    return 2 * (p * l + p * l + l * t)

def kubus(s):
    return 6 * s**2

def tabung(r,t):
    return (2 * math.pi * r**2) + (2 * math.pi * r + t)

def kerucut(r,t):
    s = math.sqrt(r**2 + t**2)
    return math.pi * r * (r + s)

def luas_permukaan_limas(s,t_s):
    luas_alas = s**2
    luas_sisi_tegak = 2 * s * t_s
    return luas_alas + luas_sisi_tegak