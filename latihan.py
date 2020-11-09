
#latihan 1
# huruf = 'abcdefghijklmnopqrstu'
# y = input('masukan kata: ').lower()
# list_huruf = [i for i in huruf]
# rumus = list_huruf[2:]+list_huruf[:2]

# # print(rumus) 
# output = ''

# for i in y :
#     if i == ' ':
#         output += ' '
#     elif i in huruf:
#         output += rumus[list_huruf.index(i)]
#     else:
#         break 
# print(f'hasil dari {y.upper()} adalah {output.upper()} ')

#latihan 2\


n = int(input('masukan jumlah angka: '))

print()


for i in range (n):
    for j in range (n,i,-1):
        print(" ",end = "")
    for j in range (2*i+1):
        print("*",end = "")
    print()

# for i in range(a-1):
#     for j in range(a,i,-1):
#         print(' ',end= '')
#     for j in range (2*1+1):
#         print('*', end= '')
#     print() 

# for i in range (n-1,-1,-1):
#     for j in range (n,i,-1):
#         print(" ",end = "")
#     for j in range (2*i+1):
#         print("*",end = "")