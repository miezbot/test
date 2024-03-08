#Print Biasa Hello World
print("Hello World!")

#Print Menggunakan Parameter Tambahan


#Seperator 
print("Hello","Selamat", "siang", " ", sep="kntl ")


#End

#\n = New Line
#\t = Tab

print("Hello World", end="\n")
print("Hello World 2")


#File

#Mode Open File
# r = Read
# w = Write atau menimpa teks, jika tidak ada filenya akan membuat file baru.
# a = Append, ini adalah untuk menamahkan teks pada baris terakhir, jika tidak ada filenya akan membuat file baru.
# + = ini untuk menggunakan mode secara bersamaan seperti 2 mode sekaligus

rangga = open("ranggay.txt",'r')
print("Isi dari file hello adalah", rangga.read())
rangga.close()


#Flush

# print("Hello, world!", flush=True)




import sys 
print("hello world tanpa flush")
print("hello world tanpa flush")
print('Hello World Flush', flush=True)






# Print Concatenated

print("Hello" + " World")

#Print Formatting

a = "Ucup"
b = "Alip"
c = 12
                #a                      #b
print('Halo saya {}, dan ini teman saya {}, dan kami berumur {}'.format(b,a,c))

print(f'Halo nama saya {a}, dan ini teman saya {b}, dan kami berumur {c}')




