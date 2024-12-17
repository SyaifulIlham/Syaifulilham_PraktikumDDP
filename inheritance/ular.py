from hewan import hewan

class ular(hewan):
    def __init__(self,nama,makanan,hidup,berkembang_biak,warna, jenis, berbisa):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.jenis = jenis
        self.berbisa = berbisa
    
    def info_ular(self):
        super().info_hewan()
        print(f"warna : {self.warna}",
              "\njenis :\t",self.jenis,
              "\nberbisa :\t",self.berbisa)
        print("=========================================================")
        
kobra = ular("Kobra","daging","semak-semak dan hutan","bertelur","hitam","ular ganas","iya")
kobra.info_ular()
