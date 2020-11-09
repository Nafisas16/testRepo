#dictionary ='key', 'value'

employee = {
#   key : value
    'nama' : 'Andy',
    'usia' : 20,
    'married' : True,
    'jabatan' : 'IT engineer',
    'kendaraan' : ['mobil','motor'],
    'address' : {
        'street' : 'jalan mawar',
        'rt' : 5,
        'rw' : 2,
        'zipcode' : 41181,
        'geo': {
            'lat' : 12345.2344,
            'long' : 1233245.123234
        }
    }
}
print(employee)
print("value dalam key 'nama' adalah:", employee['nama'])
print("value dalam key 'kendaraan' adalah: ",employee['kendaraan'])
print("value dalam key 'kendaraa di index pertama adalah: ",employee['kendaraan'][0])
print("value dalam key 'address' adalah: ",employee['address'] )
print("valuse dalam key 'address' adalah: ",employee['address']['street'] )


# print(list(employee.keys()))
# print(list(employee.value())

#memakai .get
print(employee.get('nama'))
print(employee.get('gaji')) # krn ga ada di dict maka hasil akan 'none'
print(employee.get('gaji','key not found')) # gaji tidak ada di dict maka hasilnya akan 'key not found'

# assign value baru ke key yg juga baru
employee['gaji'] = 2000000
print(employee)

#update value di key yang sudah ada
employee['gaji'] = 3000000
print(employee)
employee['kendaraan'].append ('scooter') # merubah isi value langunsg .append (tidak perlu memangil employee)

# .update untuk mengupdate key dan value
employee.update ({'NIK': 92131231, 'BPJS' :10000002121})
print(employee)

# .items
print(list(employee.items())) # membuat list di setiap item 
print(list(employee['address'].items()))
print(employee['address']['geo'].items())

# mencari value apakah ada di dictionary atau tidak
print('cari value 3.000.000 ada atau tidak?: ', 3000000 in employee.values())

# CONTOH mencari value terkecil atau tertinggi di dalam dictionary
nilai_ujian = {
    'fisika' : 85,
    'matematika' : 65,
    'sejarah' : 70
}

print('mata kuliah yang  nilainya paling kecil adalah: ',min(nilai_ujian, key=nilai_ujian.get))
print('mata kuliah yang nilainya paling besar adalah: ', max(nilai_ujian, key=(nilai_ujian.get)))

# mengganti nama key
employee['alamat'] = employee.pop('address') # untuk mengganti dict keys maka diperlukan memanggil employee.pop(tidak bisa lgsg .pop)
print(employee)

# menggabungkan 2 dictionary
dic1 = {'ten' : 10, 'twenty' : 20,'thirty' : 30}
dic2 = {'forty' : 40, 'fifty' : 50, 'sixty' : 60}

# .update cara1
dic3 = dic1.copy()
dic3.update(dic2)
print(dic3)

# .update cara2
dic1_dic2 = {**dic1 , **dic2}
print(dic1_dic2)

# zip = untuk menyatukan based om index itterable(list,tuple,set)  1 denga  itterable yang lain (memuat 2 buah dictionary dari 2 list)
key = ['ten', 'twenty', 'thirty']
value = [10,20,30]

sample_dic = dict(zip(key, value))
sample_dic_reversed = dict(zip(value,key))
print(sample_dic)
print(sample_dic_reversed)

sample_list = list(zip(key, value))
print('ini sample list' , sample_list)

sample_tuple = tuple(zip(key, value))
print(sample_tuple)

sample_dic_test = {*key , *value}
print(sample_dic_test)

# memulai/ initialize dictionary dengan default values
karyawan = ['doni', 'aryo','brian']
default = {'designation' : 'application developer', 'salary' : 5000000}

res_dic  = dict.fromkeys(karyawan, default)
print(res_dic)

print(res_dic['doni'])

#quiz 1
# hari = input('masukan hari: ').lower()
# days = {
#     'senin' : 'sunday',
#     'selasa' : 'tuesday',
#     'rabu' : 'wednesday',
#     'kamis' : 'thursday',
#     'jumat' : 'friday',
#     'sabtu' : 'saturday',
#     'minggu' : 'sunday'
# }
# print('bahasa inggris dari',hari.lower(),'adalah: ',days[hari].lower())

#quiz 2

# hari = input('masukan hari (INA/ENG): ')
# days = {
#     'senin' : 'monday',
#     'selasa' : 'tuesday',
#     'rabu' : 'wednesday',
#     'kamis' : 'thursday',
#     'jumat' : 'friday',
#     'sabtu' : 'saturday',
#     'minggu' : 'sunday'
# }
# INA = list(days.keys())
# ENG = list(days.values())
# # print(INA)
# # print(ENG)
# if hari in INA:
#     print(f'bahasa inggris dari{hari} adalah: {days[hari]}')
# elif hari in ENG:
#     print(f'bahasa indonesia dari {hari} adalah: {INA[ENG.index(hari)]}')
# else:
#     print('adadsdf')