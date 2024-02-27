# ask user input for how many blacks, colors and whites are in their laundry basket
# print wash ---- where -- equals the one with the most amount of clothes items
# if there are two the same, say choose either --- or `----`


black_clothes = int(input("How many items of black clothing need washing:  "))
color_clothes = int(input("How many items of color clothing need washing:  "))
white_clothes = int(input("How many items of white clothing need washing:  "))

clothes = [black_clothes, color_clothes, white_clothes]

if black_clothes == max(clothes): 
    print("You need to wash blacks")
elif color_clothes == max(clothes): 
    print("You need to wash colors first")
else: 
    if (black_clothes >= color_clothes): 
        print("You need to wash whites first, then blacks ( {} items) and then colors ( {} items)".format(black_clothes, color_clothes))
    
    else: 
        print("You need to wash whites first, then ( {} items) and then ({} items)".format(color_clothes, black_clothes))
