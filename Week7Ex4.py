print("Press enter when you finnish with your list!")
shopping = []
while True:
    items = input("Please enter the shopping items: ")
    shopping.append(items)
    if items == '':
        shopping.remove(items)
        print("Your shopping list is done, have a quick look!")
        print(shopping)
        break
    
