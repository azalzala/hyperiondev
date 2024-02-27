
# A programme capable of storing location and radiation level data, as well as generating descriptive stats for Dr. Eleanors radiation experiment.

# Import library for stats operations
import numpy as np


# Use lists to store data because of their versatility, low memory usage and fast data accession.
location = ['City Center', 'Industrial Zone', 'Residential District', 'Rural Outskirts', 'Downtown']
radiation = [
    [22, 19, 20, 31, 28],
    [35, 32, 30, 37, 40], 
    [15, 12, 18, 20, 14],
    [9, 13, 16, 14, 7],
    [25, 18, 22, 21, 26]]


for i, x in enumerate(location):  
    average = sum(radiation[i]) / len(radiation[i])
    print(f" {average}, {location[i]}")
    print("Standard Deviation \n")
    std_value = np.std(radiation[i])
    print(f" {std_value}, {location[i]}")

while True: 
    level = input("enter radiation or 'done' to finish: ") 
    place = input("enter location of collection: ")
   # check for done, otherwise continue   
    if level.lower() == "done": 
        break 
    try:   
    # check whether the location for the new observation exists 
        for i, x in enumerate(location):  
            if x == place: 
            # if the location matches a known sample site, add the measurement to the radiation list.
                radiation[i].append(int(level))
    # add the new measurement to the list at the same index 
                print(f"{location[i]} has a new measurement, updated list {radiation[i]}" )
    except ValueError:
    # Alert on invalid input 
        print("Invalid Input")

#Using a dictionary 

# res = dict(map(lambda i, j: (i, j) , location, radiation))
# city = [22, 19, 20, 31]

# for i in res: 
#     print(sum(res[i])/len(res[i]))

measurements = { 'Trial 1':  { "City Center": [22, 19, 20, 31, 28] }, 

'Trial 2':  {"City center": [15, 12, 18, 20, 14]}
    
}

for i, x in enumerate(measurements):
    print(measurements.values())

