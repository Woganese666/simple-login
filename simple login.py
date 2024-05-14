#Bretts simple login code for Gelos 14.05.24

import random #Importing the random module for generating random values
import string #Importing the string module for string-related operations
import time #Importing the time module for time-related operations

existing_users_file = "accounts.txt" #File name to store existing user information
user_credentials = {'admin': 'admin'} #Dictionary to store username-password pairs
user_roles = {'admin': 'admin'} #Dictionary to store user roles

def generate_password(length=10, use_letters=True, use_digits=True, use_symbols=True): # Function to generate a random password
    characters = ''

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def check_existing_users(username):  #Function to load existing users from the file and check if the username already exists
    with open(existing_users_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            user, _ = parts
            if user == username:
                return True
    return False
def save_user(username, password): #Function to save a new user to the file
    with open(existing_users_file, "a") as file:
        file.write(f"{username} {password}\n")
def login(): # Function to handle user login
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_credentials.get(username) == password: #Check if the username and password match the ones in user_credentials
        print("Login successful!")
        if user_roles.get(username) == 'admin':
            print("Welcome Admin! You have access to account information.")
            admin_menu()
        else:
            print("You have successfully logged in.")
        return username

    if check_existing_users(username): #If not found in user_credentials, it checks the existing_users_file
        with open(existing_users_file, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 2:
                    user, stored_password = parts
                    if user == username and stored_password == password:
                        print("Login successful!")
                        if user_roles.get(username) == 'admin':
                            print("Welcome Admin! You have access to account information.")
                            admin_menu()
                        else:
                            print("You have successfully logged in.")
                        return username

    print("Invalid username or password. Please try again.")
    return None

def register(): #registers a new user account
    while True:
        username = input("Enter your username: ")

        if check_existing_users(username):
            print("Username already exists. Please choose another one.")
        else:
            break

    choice = input("Do you want to create your own password? (yes/no): ").lower()
    if choice in ['yes', 'y']:
        while True:
            password = input("Enter your password: ")
            if len(password) < 10:
                print("Password length needs to be a minimum of 10 characters")
            else:
                break #exits the loop if password is valid
    elif choice in ['no', 'n']:
        while True:
            length = int(input("Enter the length of the password: "))
            if length < 10:
                print("Password length needs to be a minimum of 10 characters")
            else:
                break #exits the loop if password is valid

        use_letters = input("Include letters? (yes/no): ").lower() in ['yes', 'y']
        use_numbers = input("Include numbers? (yes/no): ").lower() in ['yes', 'y']
        use_symbols = input("Include symbols? (yes/no): ").lower() in ['yes', 'y']

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("Your generated password is:", password)
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

    save_user(username, password)
    print("Sign up successful!")
def main_menu(): # Main function to display the main menu and handle user choices
    while True:
        print("\nWelcome to the Gelos Main Menu. Please select from one of the following:")
        print("A. Login")
        print("B. Register")
        print("C. Exit")
        choice = input("Enter your choice: ")

        if choice in ['A','a']:
            username = login()
            if username:
                logged_in_menu(username)
        elif choice in ['B','b']:
            register()
        elif choice in ['C','c']:
            print("Exiting...Have a nice day!")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please enter a letter from A to C.")
def logged_in_menu(username): # Function to display logged-in user menu and handle user choices
    while True:
        print("\nGelos Logged In Menu:")
        print("A. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice in ['A','a']:
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter A or B.")

def admin_menu(): # Function to display admin menu and handle admin choices
    while True:
        print("\nGelos Admin Menu:")
        print("A. View Accounts")
        print("B. Exit to Logged In Menu")
        choice = input("Enter your choice: ")

        if choice in ['A','a']:
            print("Accounts:")
            with open(existing_users_file, "r") as file:
                for line in file:
                    parts = line.strip().split(" ", 1)
                    if len(parts) >= 2:
                        username = parts
                        print(f"Username: {username}")
                    else:
                        print("Invalid format in file.")
        elif choice in ['B','b']:
            print("Returning to Logged In Menu...")
            break
        else:
            print("Invalid choice. Please enter A or B.")

main_menu() # Call the main_menu function to start the program
