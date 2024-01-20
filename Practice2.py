#Exercise 1: Accept numbers from a user

"""a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

print(a*b)"""

#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
"""print('Name', 'Is', 'James')
print('Name', 'Is', 'James', sep="**")"""

#Exercise 3: Convert Decimal number to octal using print() output formatting
"""num = int(input("enter the number:"))
print("%o" %num)"""

#Exercise 4: Display float number with 2 decimal places using print()
"""num = float(input("Enter the number:"))
print("%.2f" %num)"""

#Exercise 5: Accept a list of 5 float numbers as an input from the user
"""numbers = []

for i in range(5):
    item = float(input("Enter the float number:"))
    str(item)
    numbers.append(item)

print(numbers)"""

#Exercise 6: Write all content of a given file into a new file by skipping line number 5
"""
with open("C:\\Users\\rajan\\Desktop\\test.txt","r") as fp:
    lines = fp.readlines()

with open("C:\\Users\\rajan\\Desktop\\newtest.txt","w") as fp:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1
"""

#Exercise 7: Accept any three string from one input() call
"""str1,str2,str3 = input("Enter the strings:").split()
print(str1)
print(str2)
print(str3)"""
