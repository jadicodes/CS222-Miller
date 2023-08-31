# Jadi Miller 8/30/2023
# Prompt: Write a program that uses a loop to compute
# and print the sum of all 0dd numbers between 1 and 100 (inclusive).

def counter_odd():
    number = 0
    sum = 0
    for number in range(1,101,2):
        sum = number + sum
    print(sum)

counter_odd()