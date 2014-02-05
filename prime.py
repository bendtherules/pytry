import math as m
tot=0
def is_prime(x):
    for count in range(2,int(m.sqrt(x))+1):
        if x%count==0:
            #print(count)
            return False
    else:
        return True
def is_odd(x):
    return not (x%2==0)

max=300

for count1 in range(1,max):
    if is_odd(count1) and not is_prime(count1):
        print(count1)
        tot+=1


print(tot)