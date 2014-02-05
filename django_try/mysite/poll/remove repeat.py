def remove_dup(line):
    words=line.split()
    final=""
    check=words[0]
    final+=check
    for word in words[1:]:
        if word!=check:
            final+=" "+word
            check=word
    answers.append(final)

answers=[]
f=open(r"C:\Users\Abhas_2\Desktop\input(1).txt")
times=input()
for count in range(times):
    remove_dup(raw_input())
for answer in answers:
    print(answer)