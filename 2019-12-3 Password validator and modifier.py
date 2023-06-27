#Dominik Zimny
#3/12/2019
import Passwordmodule as check

try:
    username = input("Username: ")
    passwordEntered = input("Password: ")
    location = check.passwordLocations[username]
    start = int(location[0])
    end = int(location[2::])

    passwords = open("Passwords.txt")
    password = passwords.read()
    passwords.close()
    password = password[start:end]
    if password == passwordEntered:
        print("Enter")
        change = input("Change password? [y/n] ")
        if change == "y":
            passwords = open("Passwords.txt", "w")
            newPassword = input("Enter new password ")
            passwords.write(newPassword)
    else:
        print("Incorrect password")
finally:
    passwords.close()
