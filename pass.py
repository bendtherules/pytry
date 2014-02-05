numb=0;
print("Type your super awesome password")
i=raw_input()
i.lower()
for letters in i:
    l=ord(letters)-ord('a')+1
    for count in range(l):
        numb=numb*10+1
    #print numb
print ("Take this bitch!! : "+str(numb))
