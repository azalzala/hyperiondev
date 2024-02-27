#Given a dictionary of people, like the one above, 
#returns a new dictionary that contains only the people who play a certain instrument. 
#You can test this exercise with function number 6.



Mark = {'age': 56, 'height': "156cm", "weight": "64kg"}
Res = {'age': 56, 'height': "156cm", "weight": "64kg"}
Poog = {'age': 56, 'height': "156cm", "weight": "64kg"}
Lorali = {'age': 56, 'height': "156cm", "weight": "64kg"}

people = { 
    "Mark": Mark, "Res": Res, "Poog": Poog, "Lorali": Lorali
}

def find_people(dictionary, attribute_to_find): 
    i for i in people if attribute_to_find in people['height']
    dictionary.get[dictionary] = attribute_to_find 