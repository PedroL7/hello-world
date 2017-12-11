def pagetest(a):
    isEven = False
    if a % 2 == 0:
        isEven = True
    return isEven

def main():  
    a = int(input("What is the page number?"))
    if pagetest(a):  
        print("number left")
    else:
        print("number right")
main()    
    
