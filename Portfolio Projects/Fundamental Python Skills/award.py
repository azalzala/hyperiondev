# determine which award an athlete receives based on total time taken between three events 

# Ask times for events 
#calculate sum of time for completion and print total time
#if time is under or equal to 100, print x 
#elif for 2 more time conditions and last is else (max = no award)


swimming = int(input("How many minutes did you take to complete the swimming course? Answer with number of minutes: "))
running = int(input("How many minutes did you take to complete the running course? Answer with number of minutes: "))
cycling = int(input("How many minutes did you take to complete the cycling course? Answer with number of minutes: "))

triathlon = [swimming, running, cycling]
total_time = sum(triathlon)
print("It took you {} minutes to complete the triathlon".format(total_time))

if (total_time >= 100): 
    print("You have received the Provincial Colors award for your exceptional performance!")

elif (total_time <= 105) and (total_time >= 101): 
    print("You have received the Provincial Half Colors award for your amazing performance!")

elif (total_time <= 110) and (total_time >= 106): 
    print("You have received the Provincial Scroll award for your very good performance!")

else: 
    print("You qualified outside of awarded times. Try again next triathlon!")



 