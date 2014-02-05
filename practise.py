f=open(r"pyFun\base.py")
count=0
numb=[]
for index,line in enumerate(f):
    if line.strip()=="" or line.strip().startswith("#") or line.strip().startswith("'''") or line.strip().startswith("@"):
        numb.append(index+1)
        count+=1;
print str(numb)
print "Total useless lines "+str(count)