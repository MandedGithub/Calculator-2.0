num1 = input("Enter a number:")
num2 = input("Enter a number:")

ch = input("Which format would you like to choose? +,-,*,/:") 
result = 0
if ch == "+": 
    result = float(num1) + float(num2)
elif ch == "-":
    result = float(num1) - float(num2)
elif ch == "*":
    result = float(num1) * float(num2)
elif ch == "/":
    result = float(num1) / float(num2)

else: print("Invalid Format!")

print(num1, ch , num2, ":", result)