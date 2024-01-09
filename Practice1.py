#Calculate the multiplication and sum of two numbers

"""def multiplyNumbers(num1,num2):
    product = num1 * num2
    return product

def sumNumbers(num1,num2):
    sum = num1 + num2;
    return sum

print("please enter the first number:")
x = int(input())
print("please enter the second number")
y = int(input())

result1 = multiplyNumbers(x,y)
result2 = sumNumbers(x,y)
print("The product of the number is ",result1)
print("The sum of the number is ", result2)"""

# Exercise 2: Print the sum of the current number and the previous number

"""previousnumber = 0

print("please input the range")
therange = int(input())

for i in range(therange):
    previousnumber = i
    currentnumber = previousnumber + 1
    sum = previousnumber + currentnumber
    print("currentnumber:",currentnumber,"previousnumber:",previousnumber,"sum:",sum)"""

# Exercise 3: Print characters from a string that are present at an even index number

"""print("please enter your desired string")
thestring = input()

thelist = list(thestring.strip())
print(thelist)

for i in range(len(thelist)):
    if (i%2==0):
        print(thelist[i])"""

#Exercise 4: Remove first n characters from a string

"""print("please input your desired string:")
thestring = input()
thelist = list(thestring.strip())

print("how many items do you want to remove")
items = int(input())
for i in range(items):
    thelist.remove(thelist[i])

print(thelist)"""

# Exercise 5: Check if the first and last number of a list is the same
"""thelist = [10,30,12,23,56,534,67,10]



if(thelist[0] == thelist[len(thelist)-1]):
    print("it is same")
else:
    print("it ain't same")"""

# Exercise 6: Display numbers divisible by 5 from a list
"""thelist = [5,10,20,33,44,5]
print("numbers divisible by 5:")
for num in thelist:
    if(num % 5==0):
        print(num)   """

#Exercise 7: Return the count of a given substring from a string
"""thestring = input("please enter the string:")
thelist = thestring.split()
print(thelist)
theword = input("please enter the word that you want to count:")
count = 0
for i in thelist:
    if i==theword:
        count = count + 1
print(theword," came ",count," times.") """

#Exercise 8: Print the following pattern
"""print("The pattern is here:")

for i in range(5):
    for j in range(i):
        print(i, end='')
    print("\n") """

#Exercise 10: Create a new list from two list using the following condition
"""def merge_list(list1,list2):
    result_list=[]

    for num in list1:
        if(num % 2 != 0):
            result_list.append(num)

    for num in list2:
        if(num % 2 == 0):
            result_list.append(num)
    
    print(result_list)

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

merge_list(list1,list2)"""

#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

"""x = int(input("Enter the digit:"))

while x>0:
    b = x%10
    x=  x//10
    print (b, end=" ")"""

#Exercise 12: Calculate income tax for the given income by adhering to the rules below

"""x = int(input("enter your income:"))
tax = 0

if x>10000:
    a = x-10000;
    if a>10000:
        b = a-10000;
    elif:

        tax = b*0.2 + 10000*0.1

print(tax)"""

#Exercise 13: Print multiplication table from 1 to 10
"""print("The multiplicaiton table is:")

for a in range(1,10):
    print(a, end="\n",)
    for b in range (1,11):
        print(a*b, end=" ") """

#Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
"""print("The Half Pyramid Triangle is here:")
for i in range(5,1,-1):
        for j in range(i,0,-1):
            print("*", end=" ")
        print(" ")"""

#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
"""def exponent(base, exp):
    result = 1;
    for i in range(exp):
        result = result * base
    print(result)

exponent(2,4) """




