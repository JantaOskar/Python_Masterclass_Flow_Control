# Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
# Note that zero is considered to be divisible by all other integers, so your output should include zero.

for i in range(101):
    if i % 7 == 0:
        print(i)

