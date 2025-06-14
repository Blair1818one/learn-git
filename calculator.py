print("1 addition")
print("2 subtraction")
print("3 muliplication")
print("4 division")

choice = input("Enter your choice : ")

num1 = float (input("Enter Number 1 : "))
num2 = float (input("enter Number 2 : "))

if choice == "1":
    print("the sum is ", num1 + num2)
elif choice == "2":

    print("the difference is ", num1 - num2)
elif choice == "3":

    print("the priduct is ", num1 * num2)
elif choice =="4":

    if num2 ==0.0:
        print("divide by 0 error")
    else:
        print(num1, "/", num2, "=", num1 / num2)

else:
    print("(Invalid choice)")

