# Create a login page backend to ask users to enter the username
# and password. Make sure to ask for a Re-Type Password and if the
# password is incorrect give a chance to enter it again but it should
# not be more than 3 times.

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    retype_password = input("Re-Type password: ")
    
    attempts = 1
    while password != retype_password:
        if attempts >= 3:
            print("Too many attempts. Please try again later.")
            return False
        print("Passwords do not match. Please try again.")
        retype_password = input("Re-Type password: ")
        attempts += 1
    
    print("Login successful!")
    return True

def main():
    print("Welcome to the Login Page")
    login()

if __name__ == "__main__":
    main()
