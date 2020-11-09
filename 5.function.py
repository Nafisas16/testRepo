#f(x) = 2x + 3
#f(3) = 2(3) + 3
#f(3) = 9

# function hello wrold
# def hello():
#     print("hellow world!")

# hello()

# function pangkat 2
# def power():
#     print(3**2)
# power()

# function 1 parameter
# def power2(x):
#     print(x**2)

# power2(2)

# function 1 parameter menggunakan return

# def power2(x):
#     print(x**2)
#     return(x**2) # untuk menyimpan ke sebuah variabel agar dapat di panggil

# hasil_power2 = power2(4)
# print('print dari luar function', hasil_power2)

# function 2 parameter
# def power3(angka, pangkat):
#     return (angka ** pangkat)

# hasil_power3 = power3(3, 4)
# print('hasil dari function 2 parameter adalah: ', hasil_power3)

#quiz 1 (cara 1 biasa)
# x = int(input('masukan angka, sebelah kiri: '))
# o = input('masukan operator (x,-,x,/,^): ')
# y = int(input('masukan angka, sebalah kanan: '))

# def calculator(x , o, y):
#     if o == '+':
#         print(f'hasil penjumlahan dari {x}{o}{y} adalah {x+y} ')
#     elif o == '-':
#         print(f'hasil pengurangan dari {x} {o} {y} adalah {x - y}')
#     elif o == 'x':
#         print(f'hasil perkalian dari {x} {o} {y} adalah {x * y}')
#     elif o == '/':
#         print(f'hasil pembagian dari {x} {o} {y} adalah {x / y}')
#     elif o == '^':
#         print(f'hasil pangkat dari {x} {o} {y} adalah {x ** y}')
#     else:
#         print('invalid number')
# calculator(x , o, y)

#cara 2
# x = int(input('masukan angka, sebelah kiri: '))
# o = input('masukan operator (+,-,x,/,^): ')
# y = int(input('masukan angka, sebelah kanan: '))

# def calculator(x , o , y):


#     penjumlahan = x + y
#     pengurangan = x - y
#     perkalian = x * y
#     pembagian = x / y
#     pangkat = x ** y

     # print(f'penjumlahan {penjumlahan}, pengurangan {pengurangan}, perkalian {perkalian} ,pembagian {pembagian}, pangakt {pangkat}')
#     return penjumlahan, pengurangan, perkalian, pembagian, pangkat

# hasil1, hasil2, hasil3, hasil4, hasil5 = calculator(x, o, y)
# if o == '+':
#     print(f'hasil penjumlahan {x} {o} {y} adalah {hasil1}')
# elif o == '-':
#     print(f'hasil pengurangan {x} {o} {y} adalah {hasil2}')
# elif o == 'x':
#     print(f'hasil perkalian {x} {o} {y} adalah {hasil3}')
# elif o == '/':
#     print(f'hasil pembagian {x} {o} {y} adalah {hasil4}')
# elif o == '^':
#     print(f'hasil pangkat {x} {o} {y} adalah {hasil5}')
# else:
#     print('data tidak dapat ditemukan,coba kembali')


# beta()['hello'][2]()()[1][2]['test']()
# x = 2
# a = str(x)
# # print(a)
# y = 1
# b = str(y)
# print(b)
# def beta():
#     return 'hello'
# a_list = [beta,2,1,2,'test']
# a_list.pop()
# print(a_list)
# print(a_list[0]())











