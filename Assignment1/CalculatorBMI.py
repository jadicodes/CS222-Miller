# Jadi Miller 8/30/2023
# Prompt: Write a program that calculates a person's BMI using their weight and height
# and tells them whether they are overweight, underweight, or optimal weight.

def bmi_calculator():
    print("Input your weight:")
    weight = input()
    weight = float(weight)
    print("Input your height in inches:")
    height = input()
    height = float(height)
    BMI = ((weight * 703) / (height*height))
    print ("Your BMI is " + str(BMI) + ".")
    BMI = float(BMI)
    return BMI

def bmi_status():
    BMI = bmi_calculator()
    if (BMI > 25):
        print("You are overweight.")
    elif (18 < BMI < 25):
        print("Your BMI is optimal.")
    else:
        print("You are underweight.")

bmi_status()