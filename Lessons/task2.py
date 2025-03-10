sentence = "I study at Khazar University"
sentence = sentence.replace(" ", "")
a = []
for i in range(0,len(sentence),2):
    a.append(sentence[i:i+2])
print(a)
print(" ".join(a))