# Python program that keeps adding numbers given number until you quit, 'q' 

sum = 0 
print("Welcome to Apni Dukan")
while(True):
    
    userinput = (input("Enter the price or press q to exit and total\n"))
    if userinput != 'q':
        sum = sum + int(userinput)
        print(f"order value till now {sum}")
    else:
        print("Thanks for shopping with us")
        print(f"Our total price is {sum}")
        print("Have a great day ahead")
        break



