def primeno(num, i):
    if(i==1):
        return 1
    elif(num%i==0):
        return 0
    else:
        return primeno(num,i-1)

     


input_no=input('Enter the number')
var=primeno(input_no,input_no/2)
if var==1:
    print 'Its Prime'
else:
    print'Not prime'
