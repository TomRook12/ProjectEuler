'''Hardest, a function to recognise a palindrome,
Start with code example, 91*99= 9009'''

chop1 = ""
chop2 = ""
palindromelist = []

for a in range(100, 1000):
    for b in range(100, 1000):
        num = (str(a * b))
        chop1 = num[:len(num) // 2]
        chop2 = num[len(num) // 2:]
        if chop1 == chop2[::-1]:
            palindromelist.append(num)

print(max(palindromelist))
