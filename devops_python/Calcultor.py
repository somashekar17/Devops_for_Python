num_1=float(input("Enter the first number"))
num_2= float(input("Enter the second number"))
choice=input("Enter the operator (+ - * /):")
if choice =="+":
    add=num_1+num_2
    print("Addition:", choice)
elif choice =="-":
    sub=num_1-num_2
    print("Subtraction:", sub)
elif choice == "*":
    mul=num_1*num_2
    print("Multiplication:", mul)
elif choice=="/":
    div=num_1/num_2
    print("Division:", div)
else:
    print("Invalid choice")