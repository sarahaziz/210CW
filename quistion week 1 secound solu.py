


def TrailingZero(x):
    count=0
    for number in range(2,x+1):  
        while number>0: 
            if number%5==0:
                count+=1
                number=number/5
            else:
              break
        return count
var=TrailingZero(5)
print var
   
