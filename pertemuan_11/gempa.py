class gempa:
    def __init__(self,location,scale):
        self.location = location
        self.scale = scale
        
    def hitungdampak(self):
        if self.scale < 2:
            print("dampak gempa gak berasa")
        elif self.scale >=2 and self.scale <= 4:
            print("dampak gempa terasa dengan bangun retak retak")
        elif self.scale >=4 and self.scale <= 6:
            print("dampak gempa bangunan roboh")
        elif self.scale > 6:
            print("dampak gempa bangunan roboh dan berpotensi tsunami")
            
        print(f'lokasi gempa : {self.location}')
        print(f'skala gempa : {self.scale}')