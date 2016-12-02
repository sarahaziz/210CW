def remove(string):
    if len(streing)==0: 
        return string  
    else:
        newstring=string[1:len(string)+1]
        firstletter=string[0]

        if firstletter in 'aeiouAEIOU':

            return remove(newstring)

        else :
            return firstletter + remove(newstring)


print remove('Beautiful')
