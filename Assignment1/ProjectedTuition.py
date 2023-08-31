# Jadi Miller 8/30/2023
# Prompt: At one college, the tuition for a full-time student is $8,000 per semester. 
# It has been announced that the tuition will increase by 3 percent each year for the 
# next 5 years. Write a program with a loop that displays the projected semester 
# tuition amount for each of the next 5 years.

def tuition_increase():
    tuition = 8000.0
    years = 5
    while years > 0:
        tuition = tuition * 1.03
        tuition = round(tuition, 2)
        print("In " + str(years) + " years, tuition will cost $" + str(tuition))
        years = years - 1

tuition_increase()