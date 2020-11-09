


class Sekarang:

    """
     membuat daftar hari, bulan, tahun
    
    """

    
    
    # a = {'01' : 'januari', '02' : 'februari', '03' : 'maret', '04' : 'april', '05' : 'mei','06' : 'juni', '07' : 'juli' , '08' : 'agustus', '09' : 'september', '10' : 'october', '11' : 'november', '12' : 'desember'}
    # b = {'monday': 'senin', 'tuesday' : 'selasa', 'wednesday' : 'rabu', 'thursday' : 'kamis', 'friday' : 'jum"at', 'saturday' : 'sabtu', 'sunday' : 'minggu'}
    import datetime as dt
    bulan_a = ['01','02','03','04','05','06','07','08','09','10','11','12']
    bulan_b = ['januari','februari','maret','april','mei','juni','juli','agustus','september','oktober','november','desember']

    # print(bulan_a[2])

    time = dt.datetime.now()
    tahun = time.strftime('%Y') # 4 digit

        if bulan_a == time.month :
            bulan_c = bulan_b(bulan_a.index[time.month])
            bulan = bulan_c
        else:
            bulan = 'aaaaaa'

        
    #     print(bulan_b) 
    # elif b.keys() in b == time.strftime('%A') ):
    #     hari = {b.values()}
    # else:
    #     bulan('salah')
        

    
    jam = time.strftime('%H')
    menit = time.strftime('%m')
    detik = time.strftime('%S')

    # def __init__(self, waktu, year, month, day, hours, minute, second):
    #     self.time = waktu
    #     self.tahun = year
    #     self.bulan = month
    #     self.hari = day  
    #     self.jam = hours
    #     self.menit = minute
    #     self.detik = second














#    def __init__(self, setahun, sebulan, sehari):
#         self.tahun = setahun
#         self.bulan = sebulan
#         self.hari = sehari

#     def full(self):
#         return f'{self.tahun}/{self.bulan}/{self.hari}'

     
# x = Sekarang('2020', '10', '3')   

# print(x.tahun)
# print(Sekarang.__doc__)