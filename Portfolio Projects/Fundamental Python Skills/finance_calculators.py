# Offer a choice between investment interest calculator or home loan repayment calculator
# If interest calculator is selected, request further general info from client and whether it is simple or compound interest they want to calculate. Print the total amount after interest. 
# However, if loan repayment selection is selected, ask for inputs and output the repayment quantity per month
import math 

print("\n investment to calculate the amount of interest you'll earn on your investment \n bond \t- to calculate how much you'll have to repay on a home loan")

while True: 
    choice = input("\n Enter either 'investment' or 'bond' from the menu above to proceed: ")
    choice_upper = choice.upper()
    if choice_upper == "INVESTMENT": 
        # years, deposit, interest, interest type
        deposit = int(input("Amount of money depositing: ")) 
        interest = float(input("Interest rate (%): "))
        years = int(input("Number of years for investment: "))
        interest_type = input("Which interest type would you like to see applied to your investment, simple or compound? ") 
        interest_upper = interest_type.upper()
        percentage_increase = interest /100 
        
        if interest_upper == "COMPOUND":  
            compound = deposit * math.pow((1 + percentage_increase),years) 
            print(f"With compound interest, your investment will return {compound: 0,.2f} over {years} years")
        
        elif interest_upper == "SIMPLE": 
            simple = deposit * (1 + percentage_increase * years)
            print(f"With simple interest, your investment will return {simple: 0,.2f} over {years} years")
        
        else: 
            print("Sorry, try again.")
            
    elif choice_upper == "BOND": 
        # house value, interest rate, repayment length
        
        house_value = float(input("What is the current estimated house value: "))
        interest_rate = float(input("What is your interest rate: ")) / 100
        repayment_months = float(input("Which repayment timeframe (months) are you following: "))
        # calculate monthly interest rate 
        monthly_interest = interest_rate / 12
        repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** -(repayment_months)) 

        print(f"You have to pay {repayment: 0,.2f} per month. If you need support, click the link below or talk to a service agent on +44 021 53962220.")

    else: 
        print("Error. We didn't get that. Please try re-typing whether you want a bond or investment") 

