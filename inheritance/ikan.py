from hewan import hewan

class Bird(hewan):
    def __init__(self,nama,makanan,hidup,berkembang_biak,warna, jenis, bernafas):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.jenis = jenis
        self.bernafas = bernafas
    
    def info_ikan(self):
        super().info_hewan()
        print(f"warna : {self.warna}",
              "\njenis :\t",self.jenis,
              "\nsayap :\t",self.bernafas)
        print("=========================================================")
        
arwana = Bird("Arwana","apa saja","sungai","bertelur","merah, kuning, emas, silver","ikan hias","insang")
arwana.info_ikan()
