# Calculate value (plane cost, hotel, car-rental)
import random

def main(): 
    # ask for user info: num_nights, city_flights, rental_days 
    print("We will calculate the total value of your holiday for you. \n First, I need some basic information about the trip: \n 1. number of nights \n 2.where you will be going \n 3. how many days you will need a car. \n If you don't have the numbers, leave it empty.")
    hotel = hotel_price(input("How many nights is your holiday: "))
    flights = flight_price(input("Where are you flying: "))
    rental_days = car_cost(input("How many days are you renting: "))
    holidaycost(hotel, flights, rental_days)

manchester_hotel_prices = [38.20, 65, 127.85, 46.22, 35.20, 100.90]
city_flights = { 'New York' : 500, 'Rome' : 240, 'Milan' : 150, 'Jaipur': 2000, '': 0}

# calculate hotel costs 
def hotel_price(nights=0): 
    try:
        return float(nights) * random.choice(manchester_hotel_prices)
    except ValueError: 
        return 0 
  
#calculate flight costs

def flight_price(destination=''): 

    for city in city_flights: 
        try: 
            if city == destination: 
                return city_flights[city]
        except ValueError: 
            return 0

# # calculate car rental costs 
def car_cost(days=0):
    try: 
        return float(days) * 34.20
    except ValueError: 
        return 0


# # combine all three costs within a function holidaycost, that takes three parameters 
#     # holiday cost should return total value 
#     # holiday cost should allow different combinations of parameters to be used. 

def holidaycost(hotel=0, flights=0, rental_days=0): 
    total_cost = flights + hotel + rental_days
    print(f"Total holidays cost: {total_cost}")
# # show the user their holiday cost
   
main()



