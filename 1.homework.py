## solve 1
# x = 4
# y = 3
# z = 2
# a = x + y * z
# b = x * y
# w = (a/b) ** 2
# print(a)
# print(b)
# print('hasilnya adalah',w,)

## solve2
# a = input('silahkan masukan angka berapapun :')
# b = int(a)**2
# print('kuadrat dari angka',a,'=',b )

## solve 3

# a = 485
# b = (485/360)
# c = (485/30)
# d = (485/7)
# print('hari',a,'bulan',c,'tahun',b,'minggu',d,)

# solve 4
# a =input('Nama1 :') #di soal Andi
# b =input('Nama2 :') #di soal Budi
# c =input('masukan umur a + b :')
# d =input('masukan rasio umur a dengan b :')
# c =float(c)
# d =float(d)
# print(type(c))
# print(type(d))

# x = c / (1+d)
# print(x)
# y = c - x
# print(y)

# print('Usia',a,'2 tahun lagi',float(y)+2, 'Usia',b,'2 tahun lagi',float(x)+2)



## solve5
# x = input ('String yang di buat :')
# y = input ('huruf yang ingin di cari jumlahnya :')
# print(x,'memiliki huruf',y,'sebanyak',x.count(y))


#Solve6
# a =input('Jarak mobil a dan b :')
# b =input('kecepatan mobil a :')
# c =input('kecepatan mobil b :')
# d =input ('waktu a dan b pergi :')
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))
# a =float(a)
# b =float(b)
# c =float(c)
# d =float(d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# x = a / (b+c) # waktu -> jarak mobil / kecepatan mobil a dan b
# y = x * 60 # hasilwaktu * 60 menit
# z = d * 60 #waktu start bareng * 60 menit
# e = d + x #total waktu ->> waktu start + waktu hasil hitung
# w_t = (y + z) % 60 # hasil 10.12 di mod jadi hasilnya 12.0
# print(x)
# print(y)
# print(w_t)

# import math as m
# w_tp =m.floor(e) #total waktu bertabrakan di floor 
# print(w_tp)

# print('Mobil A dan B bertabrakan pada pukul',w_tp,':', int(w_t))




# latihan class oop

# class Liburan:

#     """
#     perencanaan data liburan tahun baru
    
#     """
#     antrian = 0
#     def __init__(self, first, last, pay):
#         self.firstname = first
#         self.lastname = last
#         self.payment = pay
        
#         # hp = int(input('masukan nomor hp anda: '))
#         self.cp = hp

#         Liburan.antrian += 1
#         self.nomor = Liburan.antrian

#         self.email = (f'{self.firstname.lower()}.{self.lastname.lower()}@gmail.com')



#     def fullname(self):
#         return f'{self.firstname.lower()} {self.lastname.lower()}'

    
    

    
# orang_1 = Liburan ('nafis', 'sulthoni', 300000 )
# orang_2 = Liburan ('brian', 'latu', 300000 )
# orang_3 = Liburan ('ibnu', 'ananta', 200000 )


# print(Liburan.__doc__)

# print(orang_1.firstname)
# print(orang_1.fullname())
# print('uang yang sudah di bayar', orang_1.payment)
# print('nomor hp', orang_1.cp)
# print(orang_1.email)
# print(orang_1.nomor)


# print(orang_2.firstname)
# print(orang_2.fullname())
# print('uang yang sudah di bayar', orang_2.payment)
# print('nomor hp', orang_2.cp)
# print(orang_2.email)
# print(orang_2.nomor)

# print(orang_3.firstname)
# print(orang_3.fullname())
# print('uang yang sudah di bayar', orang_3.payment)
# print('nomor hp', orang_3.cp)
# print(orang_3.email)
# print(orang_3.nomor)
# 
# 

from waktu import Sekarang as skr


print('Waktu Sekarang: ',skr.time)
print('Tahun: ',skr.tahun)
# print('Bulan : ',skr.bulan) 
# print('Hari : ',skr.hari) 
print('Jam: ',skr.jam)
print('Menit: ',skr.menit)
print('Detik: ',skr.detik)





# import datetime as dt

# time = dt.datetime.now()
# print(time)
# print(time.month)