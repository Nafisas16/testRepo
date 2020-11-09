x = 5
y = '5'
z = 6

#contditional statement
# print(x == float(y)) #x sama dengan float(y)
# print(x == int(y)) #x sama dengan int(y) karena y string
# print(x == y)
# print(x == z)
# print(x != z)
# print(x > z)
# print(x < z)
# print(x >= int(y))
# print(x <= z)

# Materi and atau or

# RULES and
# True and true = true
# true and false = false
# false and true = false
# false and false = false

#RULES or
# true or true = True
# true or false = True
# false or true = True
# false or false = false

# flase and flase = false
# print(x == z and x == z)
# # false or true
# print(x == z or x < z)

# nilai = int(input('masukan nilai siswa: '))

# if nilai >= 80:
#     print('murid lulus')
# else:
#     print('murid harus remed')

# nilai = int(input('masukan nilai siswa: '))

# if nilai >= 80 and nilai <= 100: # if hanya 1
#     print('A')
# elif nilai >= 70 and nilai < 80: # elif bisa banyak di pakai beberapa kali
#     print('B')
# elif nilai >= 60 and nilai < 70:
# else:                            # else hanya pakai sekali
#     print('d')


# kuis 1

# angka = int(input('masukan angka: '))
# if angka % 2 == 0:
#     print(angka,'maka bilangan genap')
# else:
#     print(angka,'bilangan ganjil')


# # kuis 2
# massa = int(input('masukan berat badan anda (kg): '))
# tinggi = int(input('masukan tinggi anda (cm): '))

# imt = ((massa / tinggi) / tinggi) * 10000
# print(f'{imt} berat badan {massa} kg, tinggi badan {tinggi/100} m')
# if imt < 18.5:
#     print('berat badan anda kurang')
# elif imt >= 18.5 and imt <= 24.9:
#     print('berat badan anda ideal')
# elif imt >= 25 and imt <= 29.9:
#     print('berat badan anda berlebih')
# elif imt >= 30 and imt <= 39.9:
#     print('berat badan sangat berlebih')
# else:
#     print('anda obesitas')

# not quiz 1
# x = 3000
# jumlah_beli = int(input('berapa yang anda ingin beli? '))
# harga_bayar = (x * jumlah_beli)
# print(f'total belanja anda adalah IDR {harga_bayar}')

# if harga_bayar > 100000:
#     print(f'discon 10% menjadi {(harga_bayar)- harga_bayar * 10 / 100}')
# elif harga_bayar >= 50000 and harga_bayar <=100000:
#     print(f'diskon 5% menjadi {(harga_bayar) - harga_bayar * 5 / 100}')
# else:
#     print('anda tidak mendapatkan diskon')

## not quiz 2
# perusahaan ingin memberikan bonus kepada pegawai

# gaji_pegawai = int(input('berapa gaji anda? '))
# lama_bekerja = int(input('berapa lama pegawai bekerja? '))
# bonus = int(input('jumlah bonus: '))

# if lama_bekerja >= 10 :
#     print(f'selamat anda mendapat bonus! total gaji anda {(gaji_pegawai) + gaji_pegawai * bonus / 100}')
# else:
#     print('total gaji anda',gaji_pegawai)

## not quiz 3

# umur_user1 = input('umur user1: ')
# umur_user2 = input('umur user2: ')
# umur_user3 = input('umur user3: ')

# if umur_user1 > umur_user2 and umur_user2 > umur_user3:
#     print('user1',umur_user1,'paling tua')
# elif umur_user1 < umur_user2 and umur_user2 > umur_user3:
#     print('user2',umur_user2,'paling tua')
# elif umur_user1 < umur_user2 and umur_user2 < umur_user3:
#     print('user',umur_user3,'paling tua')
# else:
#     print('tidak ada yang lebih tua')

#not quiz 4 
total_pertemuan = int(input('total kelas yang di adakan: '))
total_att = int(input('total attendace: '))

percentage = ((total_att / total_pertemuan) * 100)
b_percentage = int(percentage)
print(b_percentage)
if percentage >= 75 and percentage <=100:
    print(f'total kehadiran anda {b_percentage} %, anda diperbolehkan mengikuti ujian')
else:
    print(f'total kehadiran anda {b_percentage} %, anda tidak diperbolehkan ujian')




