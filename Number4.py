'''Hardest, a function to recognise a palindrome,
Start with code example, 91*99= 9009'''

x = str(9009)
print(x[0])
print(x[-1])

for i in range(10, 99):
    break

while x[0] == x[-1]:
    if x[1] == x[-2]:
        palindrome = True
    if palindrome == True:
        print("PALINDROME")
        break

