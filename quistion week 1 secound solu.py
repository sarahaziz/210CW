'''
Each pair of 2 and 5 will cause a trailing zero.
Since we have only 245's, we can only make 24 pairs of
2's and 5's thus the number of trailing zeros in 100 factorial is 24.
If you like this post,
please Digg it or give it a thumbs up on StumbleUpon

'''


def TrailingZero(x):
    count=0
    for number in range(2,x+1): #1 factorial is = zero so we start from 2 
        while number>0: #if we reach to zero than the multiplication is zero 0 so nymber must be greater> than 0
            if number%5==0:#if the division result zero for the reminder than incremnt the count otherwise come out of the loop
                count+=1
                number=number/5
            else:
              break
        return count
var=TrailingZero(5)
print var
   
