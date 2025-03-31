name = "John"
number = "994552918195"
email = "email@gmail.com"
print(name.index("o"))

print(number.index("9",2,7))
print(number.count("9"))

num = "   555   "
print(num.strip()) #bosluqlari evvelden ve axirdan silir
print(number.replace(" ",""))  # bosluqlari silir

print(number.split("2")) # heminsimvola gore bolur

print(number.startswith("994")) #True or False print edir
print(email.endswith("gmail.com")) #True or False print edir

print(len(number))

print(number.removeprefix("994"))  # evvelden yazdigimiz simvolu silir
print(email.removesuffix("gmail.com"))  # sondan yazdigimiz simvolu silir

print(number[6:8])  # 6ci simvoldan 8 ci simvola kimi (8 daxil deyil)

print(number[4:10:2])  # 4ci simvoldan 10 ci simvola kimi (10 daxil deyil)  2 2 gederek

print(number[::-1])  # tersine cevirir

print(number.replace("55","77"))  # simvolu deyisir yenisi ile

