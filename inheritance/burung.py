from hewan import hewan

class Bird(hewan):
    def __init__(self,nama,makanan,hidup,berkembang_biak,warna, suara, sayap, paruh):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.suara = suara
        self.sayap = sayap
        self.paruh = paruh
    
    def info_kicau(self):
        super().info_hewan()
        print(f"warna : {self.warna}",
              "\nsuara :\t",self.suara,
              "\nsayap :\t",self.sayap,
              "\nparuh :\t",self.paruh)
        print("=========================================================")
        
merpati = Bird("Merpati","Biji-bijian","Hidup di pohon","bertelur","putih","kurang gacor","putih","kecil")
elang = Bird("Elang","daging","tebing","bertelur","putih / coklat","mengintimidasi","hitam / coklat","bengkok")
bu = Bird("Burung unta","daging","gurun","bertelur","coklat","keras","tidak punya","panjang")
merpati.info_kicau()
elang.info_kicau()
bu.info_kicau()