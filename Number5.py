'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

x = 0

for a in range (0, 1000000000000000):
    x = 0
    for b in range(1, 21):
        if a % b == 0:
            x += 1
        if x == 20:
            print(a)


