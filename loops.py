system_email= "charles@gmail.com"
system_password = "password@123"

email = input("Enter an email")
password = input("Enter the password")

if email == system_email:
    if password == system_password:
        print("Login successfull")
        print(f"welcame, {email}")
    else:
        print("Invalid password!")
else:
    print("user doesnot exist")