class hewan:
    def __init__(self, nama, makanan,hidup,berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def info_hewan(self):
        print(f"Hewan ini bernama {self.nama}\t\t",
              "\nmakanan utamanya adalah\t", self.makanan,
              "\nHidup di\t",self.hidup,
              "\nBerkembang biak dengan cara\t",self.berkembang_biak)
    