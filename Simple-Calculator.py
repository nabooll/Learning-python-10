# So we have to make function for each operation
def substraction(a, b):
    return a+b

def elimination(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def divides(a, b):
    return a/b

a = int(input("The first number: "))
b = int(input("The second number: "))
c = input("What operation are you going to use?\nchoose one (+,-,*,/)")

# Now we gotta use if else condition
if c == "+":
    ans = substraction(a, b)
elif c == "-":
    ans =elimination(a, b)
elif c == "*":
    ans = multiplication(a, b)
else:
    ans = divides(a, b)

print(f"The answer is {ans}")