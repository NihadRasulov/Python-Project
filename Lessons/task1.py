sentence = "I study in Khazar University"
sentence = sentence.replace("I", "i")
sentence = sentence.replace("U", "u")

u = sentence.count("u")
i = sentence.count("i")

if u>i:
    print("Letter u is more than i")
else:
    print("Letter i is more than u")