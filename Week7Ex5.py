sentence_1 = input("Please enter the first sentence: ")
sentence_2 = input("Please enter the second sentence: ")
concatenated = " ".join([sentence_1, sentence_2])
#List creation
list_x = concatenated.split()
list_alpha = sorted(list_x, key= str.lower)
print("The following list is sorted alphabetically!")
print (list_alpha)
print("There are %d words in this list" % len(list_alpha))

#Dictionary
my_dict = {}
print("Now I am going to see if there is any repetition of words :) ")
for word in range(len(list_x)):
    my_dict[list_x[word]] = list_x.count(list_x[word])
print(my_dict)    
for word in my_dict:
    print(word)
