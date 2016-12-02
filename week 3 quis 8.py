def remove(string):
    if len(streing)==0:#if the lenth of string you pass is 0 then return that 
        return string # the lenth function len will give the lenth of the string 
    else:
        newstring=string[1:len(string)+1]#1-string[1:len(string)+1] will give all the characters
        #2- from first character onwords 
        firstletter=string[0]

        if firstletter in 'aeiouAEIOU':

            return remove(newstring)#recursion definsation

        else :
            return firstletter + remove(newstring)# recursion


print remove('Beautiful')
