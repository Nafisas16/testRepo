## LAMBDA ##

# def perkalian(a, b):
#     print(a*b)

# perkalian(2,3)

# x = lambda a, b: a*b
# print(x(2,3))

# y = lambda a,b,c: (a/b)* c
# print(y(1,2,3))

# z = lambda a: 'genap' if a % 2 == 0 else 'ganjil'
# print(z(4))

# def penjumlahan(a,b):
#     y = lambda a, b: a+b
#     return y(a,b)

# print(penjumlahan(1,2))

## MAP ## = syarat map harus ada fucntion MAP(FUCNTION +VARIABEL OR DLL)

# name_list = 'andi budi caca'.split()

# def function(a):
#     return(len(a))

# len_list = list(map(function, name_list)) #map(fucntion, variabel or something)
# print(len_list)

# len_list2 = list(map(lambda a: len(a), name_list))
# print(len_list2)

# list_1 = 'cokelat melon naangka'.split()
# list_2 = [10000,5000,20000]
# couple_list = list(map(lambda a,b: a + str(b), list_1, list_2))
# print(couple_list)

## FILTER ##
# h = range(11)
# def kurang_lima(x):
#     if x < 5:
#         return True
#     else:
#         return False

# j = list(filter(kurang_lima,h))

# print(j)
# print(list(h))




# quiz 1

# input = [2,4,6,8]

# hsil = list(map(lambda a: a*2, input))

# print(list(hsil))

# quiz 2
# world_list = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
# word = str(input('MASUKAN KATA: '))

# j = filter(lambda a: word in a, world_list)

# print(list(j))

## reduce ##

# from functools import reduce

# number = []




from functools import reduce

print(reduce(lambda a,b: a+b, map(lambda a: a*2, filter(lambda a: a%2 ==0 , range(1,101)))))

# fizz buzz
# def fizzbuzz(y):
#         for i in range(1,y+1):
#         if i % 15 == 0:
#             print('fizzbuzz') 
#         elif i % 3==0:
#             print('fizz')
#         elif i %5 == 0:
#             print('buzz') 
#         else:
#             print(i)

# Soal 4 - setengah pyramid
# def segitiga_siku():
#     num_soal4 = ""
#     counter = 1
#     z4 = int(input("Masukan Dimensi Segitiga Bintang"))
#     for q in range(z4):
#         num_soal4 += (" * " * counter)
#         num_soal4 += "\n"  
#         counter += 1
#     print(num_soal4)

# segitiga_siku()

