'''Hardest, a function to recognise a palindrome,
Start with code example, 91*99= 9009'''

x = "9009"

mylist = [i in range(10,99)]
print(mylist)

palindrome = False
test = ''

while chop1 != chop2:
    for i in range(10,99):
        test = str(i*i)
        chop1 = test[:len(test)//2]
        chop2 = test[len(test)//2:]
        if chop1 == chop2:
            print(test)
            print("Palindrome")
        else:
            continue


'''if x[0] == x[-1]:
    if x[1] == x[-2]:
        palindrome = True
        print("PALINDROME")
'''

s = "string"
