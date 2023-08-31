# Jadi Miller 8/30/2023
# Prompt: Write a program that uses a loop to compute
# and print the sum of all even numbers between 2 and 100 (inclusive).

def counter_even():
    number = 0
    sum = 0
    for number in range(2,101,2):
        sum = number + sum
    print(sum)

counter_even()