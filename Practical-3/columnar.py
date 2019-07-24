import math

key = input("Enter Key:")
pt = input("Enter Text:")

lenkey = len(key)
lenpt = len(pt)

#----------Encryption-----------

a=0
while (lenpt % lenkey) != 0:
    a=a+1
    lenpt = lenpt + 1

for i in range(a):
    pt = pt + "*"

dict = {}
encry = ""
for i in range(lenkey):
    for j in range(i,lenpt,lenkey):
        encry = encry + pt[j]
    dict[str(i+1)] = encry
    encry = ""

dic = {}
j=0
for i in range(lenkey):
    dic[str(j+1)] = key[j]
    j = j+1

dicValue = list(dic.values())
dicValue.sort()

keyy = ""
k=0

for i in dicValue:
    for j,l in dic.items():
        if i==l:
            keyy = keyy + j
            k+=1

encryption = ""
for k in keyy:
    encryption = encryption + dict[k]

#-----------Decryption-------------

lenenc = len(encryption)

dictd = {}

decry = ""
k=0
d = int(lenenc/lenkey)
for i in range(lenkey):
    for j in range(d):
        decry = decry + encryption[k]
        k = k+1
    dictd[str(i+1)] = decry
    decry = ""

dc = ""
keyyy = ""
i=0
k=0
dicc = {}
j=0
for i in range(lenkey):
    dicc[str(j+1)] = key[j]
    j = j+1

dicValue = list(dic.values())
dicValue.sort()

for i in dicValue:
    for j,l in dicc.items():
        if i==l:
            keyyy = keyyy + j
            k+=1

for k in keyyy:
    dc =  dc + dictd[k]

decryption = ""
de = ""

l = len(dictd['1'])
ll = int(lenenc / lenkey)
for i in range(ll):
    for j in range(i,lenenc,l):
        de = de + dc[j]
    decryption = decryption + de
    de = ""

encryption=encryption.replace("*","")
decryption=decryption.replace("*","")
print("Encrypted Text: " + encryption)
print("Decrypted Text: " + decryption)
