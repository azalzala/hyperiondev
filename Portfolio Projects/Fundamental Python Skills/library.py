
book_inventory = { 
    "book 1" : {
         'copies': 2, 
         'borrowers': [] },
    "book 2": {
        'copies': 3, 
        'borrowers':[]},
    "book 3": {
        'copies':6, 
        'borrowers': []}
}

user = { 
    "user 1": { 
        'books': [],
    } } 

def main(): 
    active = login(input("What's your username"))
    x = input("Enter return or check-out: ")
    y = input("Enter book name: ")
    if x == 'return': 
        return_book(y, active)
    elif x == 'check-out': 
        gimme_book(y, active)
    else: 
        print(f"Welcome {active}")
# Create a function that returns the index/location of the user accessing their library account to update their records in the next two functions
def login(input): 

    for i in user:     
        if input == user: 
            return user[i]
        else: 
            new_acc = input("Would you like to open an account").lower()
            if new_acc == "yes": 
                username = input("Username: ")
                new_user = {username}
                user[new_user] = {'books': []}
                return user[new_user]
            else: 
                break 

# 
def gimme_book(book, user): 
# Match the name of the book with the dictionary books
    for i in book_inventory: 
        if i == book: 
            book_inventory[i]['copies'] -=1
            book_inventory[i]['borrowers'] = [].append(user)
            print(book_inventory[i])

            break
        else: 
            book_inventory[book] = {}
            
def return_book(book, user): 
   # interate through the keys in the dictionary 
    for i in book_inventory: 
        # if the book name exists
        try: 
            if i == book: 
                # add one copy to the book copies 
                book_inventory[i]['copies'] += 1
                # remove the user from the borrowers list 
                book_inventory[i]['borrowers'] = [].remove(user)
        except ValueError: 
            print("Something happened. Speak with a human pls")
        else: 
            # if the book is not found, print a message letting the user know
            print("book not found on library record")
            # once the loop evaluates the book and updates records, print the updated book attributes. 
        print(book_inventory[i])

  
# book1 = {'copies': 1, 'borrowers': []}
# books = { "Book 1": book1}
# books["Book 1"] = book1

# borrowers : []
# books['borrowers'] = [] 


