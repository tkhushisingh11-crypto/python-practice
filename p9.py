first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operation = input("choose any(+,-,*,/): ")
if(operation == "+"):
    result = first + second
elif(operation == "-"):
   result = first - second
elif(operation == "*"):
   result = first * second
elif(operation == "/"):
  result = first / second
else:
   print("Invalid operation")
   
print(result)


