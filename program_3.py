#Matthew Tyler
#10/17/25
#US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    state_info = []

    # Now have the user enter a year. 
    print("enter state population info")
    while True:
        year = int(input('Enter year or "0" to finish.'))
        if year == 0:
            break
        state = input('Enter state')
        population = int(input("Enter population"))
        state_info.append([year, state, population])
    # The program will add the populations from all states in the list of list for that year only.
    year_input = int(input("Enter year you want a total population for"))
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(state_info, year_input)
def sum_population_for_year(state_info, year_input):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    total_population = 0
    for entry in state_info:
        year, state, population = entry
        if year == year_input:
            total_population += population
    # print the totalled population
    print("The total population for", year_input, ":", total_population)


# Call the main function.
if __name__ == '__main__':
    main()
