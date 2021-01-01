#num= input("Enter number: ")this generates an error because the input function assumes it's a string type
num = int(input("Enter number: "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")