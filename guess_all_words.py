import nltk as n
from random import *
import re
word_list=n.corpus.words.words();

chr_list=[]
match_list=[]
while len(chr_list)<=9:
    temp=chr(randint(ord('a'),ord('z')));
    if temp not in chr_list:
        chr_list.append(temp);
print chr_list;

# need to make a regexp out of it
def add_str(s1,s2):return s1+s2;
reg_string="["+reduce(add_str,chr_list)+"]*"
#print reg_string;
r=re.compile(reg_string)
# after making the regexp
for w in word_list:
    if w==r.match(w).group():
        match_list.append(w);

print len(match_list);

correct_guess=[]
def check_word(word):
    if word in match_list:
        if word in correct_guess:
            return "already guessed"
        else:
            correct_guess.append(word)
            return "correct guess"
    else:
        return "wrong guess"