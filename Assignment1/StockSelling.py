# Jadi Miller 8/30/2023
# Prompt: Your company has shares of stock it would like to sell when their value exceeds
# a certain target price. Write a program that reads the target price and then 
# reads the current stock price until it is at least the target price. 
# Your program should read a sequence of floating-point values from standard 
# input. Upon reaching or exceeding the target price, your program should output 
# a message that says "Shares can be sold now".

def sell_shares(target_price):
    while True:
        current_price = float(input("Enter the current stock price: "))
        if current_price >= target_price:
            print("Shares can be sold now.")
            break

def is_target_price():
    target_price = float(input("Enter the target price: "))
    sell_shares(target_price)

is_target_price()
