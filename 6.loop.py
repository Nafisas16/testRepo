# while loops & for loops
# hanya kan menjalankan code ketika kondisisnya True

# print(1*2)
# print(2*2)
# print(3*2)
# print(4*2)
# print(5*2)
# print(6*2)
# print(7*2)
# print(8*2)
# print(9*2)
# print(10*2)

# while loops
# i = 1
# while i <= 10:
#     print(i*2)
#     i += 1

# i = 1
# while i <= 10:
#     if i <= 5:
#         print(i*2)
#     else:
#         print(i*3)
#     i += 1         # i di mulai dari 1 karena perintah i+= 1 di bawah

# i = 1
# while i <= 10:
#     i += 1 # i sudah di tambah 1 terlebih dahulu mka dimulai daari 2*2
#     if i <= 5:
#         print(i*2)
#     else:
#         print(i*3)

# i = 1
# while i <= 10:
#     i += 1
#     if i <= 5:
#         print(i*2)
#     else:
#         continue  


# tugas
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(f'{i} adalah genap')
#     else:
#         print('ganjil')
#     i += 1

# quiz 1
# i = 1
# password = '12345'

# while i <= 4 :
#     if  !== password and i <=3:
#         print('password incorrect')
#     elif  !== password and i == 4:
#         print('try again later')
#     elif  == password:
#         print('password corect')
#     else:
#         print('babay')
   

# quiz 2

# a = input('masukan kata: ')

# print(len(a))
# print(a.replace()


# quiz 3


# def factorial(n):
#     result = 1

#     if n < 0 :
#         return ('bukan jawaban')
#     else:
#         i = 1
#         while i <= n:
#             result *= i
#             i += 1
#     return result 

# n = (int(input('masukan nilai n: ')))
# print(factorial(n))

# for loops

# i = 2
# while i <= 10:
#     print(i*2)
#     i +=1

# i=1
# for i in range (1,11):
#     print(i*2)

# i=1
# for i in range (1,11):
#     print(i*2)
#     if i == 5:
#         continue
#     else


# nomor 2



# a = int(input('masukan angka: '))
# b = []
# for x in range (a):
#     y = (input(f'msaukan angka {x}'))
#     b.append(y)
#     x += 1
# print(b)
# print(b[::-1])
    

        
# jml_angka = int(input('Masukkan berapa angka: '))
# x = 1
# list_angka = []
# while x <= jml_angka:
#     input_angka = int(input(f'Masukkan angka {x}: '))
#     list_angka.append(input_angka)
#     x += 1
# print(list_angka)
# print(list_angka[::-1])







# nomor 3
# x = input('masukan kata palindrome: ')
# y = (x[::-1])


# if x == y:
#     print(f'apabila kata {x} adalah {y} maka palindrome')
# else:
#     print(f'apabila kata {x} adalah {y} maka bukn palindrome')



# jml_baris = int(input('Masukkan jumlah baris segitiga siku2: '))
# x = 1
# y = 1
# while x <= jml_baris:
#     while y <= jml_baris:
#         print('*  ' *y) 
#         y += 1
#     x += 1

# jml_baris = int(input('Masukkan jumlah baris segitiga siku2: '))
# x = 1
# y = 1
# while x <= jml_baris:
#     while jml_baris >= 1:
#         print('* '*jml_baris)
#         jml_baris -= 1
#     x += 1


# x = int(input('msukan jumlah bintang: '))
# def segitiga_siku(x):
#     star = ''
#     for i in range(x):
#         star += '*'
#         print(star)

# segitiga_siku(x)




#slicing dictionary with loop







