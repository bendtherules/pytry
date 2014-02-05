import csv
c=[89,25]
a=["hi, there ",509,c]
f=open("a.csv","w")
w=csv.writer(f)
w.writerow(a)
f.close()
f=open("a.csv","r")
r=csv.reader(f)
for c in r:
    d=c;

print(type(c))
print(c)
