import random
def my_shuffle(array): #array passed as parameters to function
    random.shuffle(array) #shuffle function will change randomly places of element

    return array

arr=[1,2,3,4]
var=my_shuffle(arr)
#calling user defined function and passing arr as argument
print var
