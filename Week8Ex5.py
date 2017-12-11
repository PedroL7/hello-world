def count_spaces(userInput):
    spaces = 0
    for char in userInput :
        if char == " " :
            spaces = spaces + 1
    return spaces        

def main():
    userInput = input("Please, enter a sentence:")
    print (count_spaces(userInput))
main()    
