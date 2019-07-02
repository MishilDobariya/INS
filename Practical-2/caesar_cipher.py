text = input("Enter plain text:")
key = input("Enter key:")
encry = []
for ch in range(len(text)):
    e = ord(text[ch])
    if(e>64 and e<91):
        e = ord(text[ch])+int(key)
        if(e>90):
            set = e-90
            e = set + 64
        encry.append(chr(e))
    if(e>96 and e<123):
        e = ord(text[ch])+int(key)
        if(e>122):
            set = e-122
            e = set + 96
        encry.append(chr(e))
#for enc in encry:
    
print("Encrypted Message:")
print(encry)

decry = []
for ch in range(len(encry)):
    d = ord(encry[ch])
    if(d>64 and d<91):
        d = ord(encry[ch])-int(key)
        if(d<65):
            set = 65 - d
            d = 91-set
        decry.append(chr(d))
    if(d>96 and d<123):
        d = ord(encry[ch])-int(key)
        if(d<97):
            set = 97 - d
            d = 123-set
        decry.append(chr(d))
print("Decrypted Message:")
print(decry)  