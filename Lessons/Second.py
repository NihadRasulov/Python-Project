age = 15
number = 12.5
name = "Nihat"
print("My name is {0}.Age is {1}".format(name, age))
print(f"My name is {name}. Age is {age}.")

print(type(age))
print(name*2)
print(age/10)  #1.5
print(age//10) #1
print(age%10) #5
print(pow(age,3))

print(format(age,"b"))  # change age to byte code
print(format(age,"o"))  # change age to octal(8-lik) code
print(format(age,"x"))  # change age to hexsadecimal(16-liq) code

# print(format(age, "02x"))

print(format(ord("A"),"b")) # daxil etdiyimiz deyiseni byte code cevirir
print(format(ord("a"),"o")) # daxil etdiyimiz deyiseni octal code cevirir

# format([fill])
print(format(name[2:], "*>5"))
print(format(name[1:len(name)-1], "*^"+str(len(name))))
print(format(name[1:7], "*^8"))
