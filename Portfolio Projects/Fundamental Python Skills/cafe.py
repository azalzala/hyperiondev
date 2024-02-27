# List menu items 
# Create dictionary with stock 
# create dictionary with prices of items
# Calculate total stock by; loop through items in the menu and multiply its price x stock, add to a count

#set an empty variable total_stock for the for loop, used at the end to calculate the sum of all the items. 

total_stock=0
menu = ['croissant', 'mocha', 'latte', 'espresso']
stock = {'croissant': 5, 'mocha': 100, 'latte': 110, 'espresso': 250} 
price = {'croissant': 1.50, 'mocha': 2.50, 'latte': 2.50, 'espresso': 1}


# Create a new list with the value of each item by looping through the dictionaries price and stock for each item in the menu    
item_value = [stock[i] * price[i] for i in menu]
print(item_value)

#Use a for loop to add all the item_values up together
for i in item_value: 
    total_stock += i

print(total_stock) 

