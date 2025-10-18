#Matthew Tyler
#10/17/25
#Rainfall

yearlyrain = []

def rain_calculation():
    global rain
    print("For the months January - December,")
    for month in range(12):
        rain = float(input("Enter rain amount:"))
        yearlyrain.append(rain)

rain_calculation()

#Calculate numbers
total_rain = sum(yearlyrain)
most_rain = max(yearlyrain)
least_rain = min(yearlyrain)
ave_rain = total_rain / 12

#Print numbers
print("The total amount of rain:", total_rain, " inches")
print("The Average amount of rain per month:", format(ave_rain, ".2f"), " inches")
print("The month with the most rain:", most_rain, " inches")
print("The month with the least rain:", least_rain, " inches")
