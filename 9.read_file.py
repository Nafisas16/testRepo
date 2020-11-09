# data = open('./nafis/kata.txt','r') 
# print(data.read())
# text = data.read()
# print(text)

# lines = data.readlines()
# print(lines)
# for line in lines:
    # print(line)




# data2 = open('./nafis/kata.txt','w')
# data2.write('ini dibuat di python')

# data3 = open('./nafis/kata3.py','w')
# data3.write("print('ini di buat di python')")

abc = open('./nafis/nama.txt','r')
# text = (abc.read()).replace(',','')
# print(text)
text_list = (abc.read()).split(',')
print(text_list)

# list_nama = open('list_nama.txt', 'w')
# for i in text_list:
#     list_nama.write(f'{i}\n')

data_diri = open ('./nafis/daftar_nama.csv', 'r')
x = data_diri.read().split('\n')
print(x)

header_list = x[0]
print('header list:', header_list)
header_element = header_list.split(',')
print('header element: ' ,header_element)

value_list = x[1:]
print(value_list)

data = [] # ['Andi,21,Jakarta', 'Budi,22,Bandung', 'Caca,23,Jakarta']
for i in value_list:
    a = i.split(',')
    header_value = dict(zip(header_element, a))
    data.append(header_value)

# print(data)

json = open('./nafis/daftar_nama.json', 'r')
print(json.read())

import json
with open('./nafis/daftar_nama.json', mode='r') as daftar:
    output = json.load(daftar)
print(output[0])
print(type(output))
for i in range(len(output)):
    print(output[i])

output.append({'nama' : 'dede', 'usia' : 24, 'kota' : 'bekasi'})

print(output)
with open('./nafis/daftar_nama_update.json', 'w') as update:
    json.dump(output, update)

import csv

list_data = []
with open('./nafis/daftar_nama.csv', 'r') as nama:
    read = csv.DictReader(nama)
    for data in read:
        list_data.append(dict(data))

print(list_data)
list_data.append({'nama' : 'dede', 'usia' : 24, 'kota' : 'bekasi'})

with open('./nafis/daftar_nama.csv','w') as update:
    columns = list_data[0].keys()
    write = csv.DictWriter(update, fieldnames=columns)
    write.writeheader()
    write.writerows(list_data)
    
print(columns)