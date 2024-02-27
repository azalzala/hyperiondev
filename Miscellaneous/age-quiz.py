age = int(input("How old are you (year): "))

if age < 100: 
    if age >= 65: 
        print("Enjoy your retirement!")
    elif age >= 40: 
        print("You're over the hill.") 
    elif age == 21: 
        print("Congrats on your 21st!")
    elif age <=13: 
        print("You qualify for the kiddie discount.")
    else: 
        print("Age is but a number")
else: 
    print("Sorry, you're dead")