# BASIC ARITHMETIC CALCULATOR

#APPROACH 1
print("Running approach 1......")

print("Select an operation to perform: ")
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")
print("5. MOD")

operation = input("Enter your choice (1/2/3/4/5): ")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if operation == '1':
    print("The sum is " + str( n1 + n2))
elif operation == '2':
    print("The sub is " + str( n1 - n2))
elif operation == '3':
    print("The mul is " + str( n1 * n2))
elif operation == '4':
    print("The div is " + str( n1 // n2))
elif operation == '5':
    print("The mod is " + str( n1 % n2))
else:
    print("Invalid Entry")
    
#----------------------------------------------------------
    
#APPROACH 2
    
print("Running approach 2......")

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
operation = input("Insert an operation (+, -, *, /, %): ")

# Construct the expression
expression = n1 + operation + n2

try:
    result = eval(expression)
    print(f"The result is: {result}")
except:
    print("invalid operation entered!!")
    

    

