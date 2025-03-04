sentence = "I study at Khazar University"
sentence = sentence.replace(" ", "")
print(sentence)

for i in range(0,len(sentence),2):
    print(sentence[i:i+2])