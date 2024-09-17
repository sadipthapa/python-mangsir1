# a=10
# def number():
#     a=11
#     print(a)
    
    
# number()
# print(a)

# a=10
# def number():
#   global a
#     a=11
#     print(a)
    
# number()
# print(a)



# a=10
# def outer():
#     a=11
#     def inner():
#         a=12
#         print("inner sees a as",a)
#         inner()
#         print('outer sees a as',a)
        
#     print('main sees a as',a)
    
#     outer()

# a=[1,2,3]
# print(a)
# a.append(12)
# print(a)


# Dictionary to store user data
user_data = {}

# Function to register a new user
def register_user():
    username = input("Enter username: ")
    
    # Check if the username already exists
    if username in user_data:
        print("Username already exists! Try a different one.")
    else:
        password = input("Enter password: ")
        # Save user credentials in the dictionary
        user_data[username] = password
        print("Registration successful!")

# Function for user login
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check if the username and password match
    if user_data.get(username) == password:
        print("Login successful!")
    else:
        print("Invalid username or password!")

# Main program using a loop
while True:
    print("\n1. Register")
    print("\n2. Login")
    print("\n3. Exit")
    
    # Lambda function to take user input choice
    choice = lambda: input("\nChoose an option: ")
    
    option = choice()
    
    if option == '1':
        register_user()
    elif option == '2':
        login_user()
    elif option == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
