#program menentukan bilangan terbesar dari tiga bua bilangan

a= int(input("Masukan bilangan pertama : "))
b= int(input("Masukan bilangan kedua : "))
c= int(input("Masukan bilangan ketiga : "))

if(a>b) and (a>c):
    print("Bilangan Terbesar adalah :",a,)
elif (b>c) and (b>a):
    print("Bilangan terbesar adalah :",b,)
elif (c>a) and (c>b):
    print("Bilangan Terbesar adalah :",c,)
