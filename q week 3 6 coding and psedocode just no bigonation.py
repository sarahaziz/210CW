sentence='Thus Is Awesome' # take the intial string 
words=sentence.split()# split method will make a list of all the words togather 
print words 
sentence_rev=''.join(reversed(words)) #-1to reverse the list make the use of reversed key word
#2- so that the words in the list will be reversed and we are joing them with the join key word in
#3- the empty string  '   '
print sentence_rev
