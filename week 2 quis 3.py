import math
def perfectsq(num):

    for i in range(1,num+1):
        c=math.sqrt(i)
        x=math.floor(c)
        if(c==x):
            print i,'Is perfect square of....>>>>:',c


print perfectsq(25)
