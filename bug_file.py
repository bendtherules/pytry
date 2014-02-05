
a=[5]
import practise
##for k in globals():
##    if not k.startswith("__"):
##        practise.globals()[k]=globals()[k]
C=practise.c(globals())
print C.pp()