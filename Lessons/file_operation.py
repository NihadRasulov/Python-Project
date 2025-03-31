"""
chmod 755  777

        read   write   execute
user      4      2        1
group     4      2        1
others    4     2       1

r,w,a,r+,w+,a+
r - file varsa oxuyur yoxdursa error verir
w - file varsa yazir yoxdursa yaradib yazir bizim yazdigimiz qeder filedan silinib sonra bizim yazdigimiz yazilir)
a- file yazi qalir sadece elave edir
r+ - file hem oxuya hem de yaza bilirik (fayl yoxdursa error verir)
w+ - file hem yaza hem de oxuya bilirik yene de fayl yoxdursa yaradir
a+ - file hem elave olunur hem de oxuya bilirik
"""

file = open('test.txt', 'w+')
file.write("hello world")
file.seek(0)   # crusorun yerini deyisirik
print(file.read())
file.flush()  # file avtomatik yazir close gozlemir
file.tell()  # crusorun yerini deyir
file.close()  # file close edildikden sonra
# error yoxdursa ozu close edir
# buffer yaddas dolanda avtomatic yazir
# file close olunmasa error bas verse fayla hec ne yazilmayacaq

with open('test.txt', 'r') as file:  # close ehtiyac yoxdur avtomatic close olunur
    file.write("hello world")
    file.truncate()  #file icerisini silir


import os
os.remove('test.txt')  # file silinir
# print(os.path.curdir)  # current directory show
os.path.isfile('test.txt') # file olub olmadigini yoxlayib boolean qaytarir