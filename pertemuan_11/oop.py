class Bank:
    norek = ''
    nama = ''
    saldo = 0
    jumlhnasabah = 0
    Bank = 'Bank Syariah Ilham'
    
    def __init__(self,no,nasabah,saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jumlhnasabah +=1
        
    def nabung(self,uang):
        self.saldo += uang
    
    def tarik(self,uang):
        self.saldo -= uang
    
    def cetak(self):
        print(Bank.Bank, 
              '\n============================',
              '\nNo. Rekening\t:',self.norek,
              '\nNama Nasabah\t:',self.nama,
              '\nSaldo\t\t     :Rp.',format(self.saldo, ','),
              '\n----------------------------',
              )
