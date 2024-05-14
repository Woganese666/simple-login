# Importing the random module for generating random values
import random

# Importing the string module for string-related operations
import string

# Importing the time module for time-related operations
import time

# File name to store existing user information
existing_users_file = "accounts.txt"

# Dictionary to store username-password pairs
user_credentials = {'admin': 'admin'}

# Dictionary to store user roles
user_roles = {'admin': 'admin'}

# Function to generate a random password
def generate_password(length=10, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to load existing users from the file and check if the username already exists
def check_existing_users(username):
    with open(existing_users_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            user, _ = parts
            if user == username:
                return True
    return False

# Function to save a new user to the file
def save_user(username, password):
    with open(existing_users_file, "a") as file:
        file.write(f"{username} {password}\n")

# Function to change the password for a user
def change_password(username):
    new_password = input("Enter your new password: ")
    user_credentials[username] = new_password
    print("Password changed successfully!")

# Function to handle user login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match the ones in user_credentials
    if user_credentials.get(username) == password:
        print("Login successful!")
        if user_roles.get(username) == 'admin':
            print("Welcome Admin! You have access to account information.")
            admin_menu()
        else:
            print("You have successfully logged in.")
        return username

    # If not found in user_credentials, check the existing_users_file
    if check_existing_users(username):
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

# Function to register a new user
def register():
    username = input("Enter your username: ")

    if check_existing_users(username):
        print("Username already exists. Please choose another one.")
        return

    choice = input("Do you want to create your own password? (yes/no): ").lower()
    if choice in ['yes', 'y']:
        password = input("Enter your password: ")
        if len(password) < 10:
            print("Password length needs to be a minimum of 10 characters")
            return
    elif choice in ['no', 'n']:
        length = int(input("Enter the length of the password: "))
        if length < 10:
            print("Password length needs to be a minimum of 10 characters")
        return

        use_letters = input("Include letters? (yes/no): ").lower() in ['yes', 'y']
        use_numbers = input("Include numbers? (yes/no): ").lower() in ['yes', 'y']
        use_symbols = input("Include symbols? (yes/no): ").lower() in ['yes', 'y']

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("Your generated password is:", password)
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        return

    save_user(username, password)
    print("Sign up successful!")

# Main function to display the main menu and handle user choices
def main_menu():
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

# Function to display logged-in user menu and handle user choices
def logged_in_menu(username):
    while True:
        print("\nGelos Logged In Menu:")
        print("A. Change Password")
        print("B. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice in ['A','a']:
            change_password(username)
        elif choice in ['B','b']:
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter A or B.")

# Function to display admin menu and handle admin choices
def admin_menu():
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

# Call the main_menu function to start the program
main_menu()
