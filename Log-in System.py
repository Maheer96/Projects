import time
import sys

def register_user():
    while True:
        username_exists = False
        username = input("Enter a new username: ")
        with open('user_database.txt', 'r') as f:
            for line in f:
                existing_users = line.strip().split(':')[0]
                if username == existing_users:
                    print("Sorry, that username already exists! Please enter a new username.")
                    username_exists = True
                    break # Exit loop if username is found

        if not username_exists:
            break # Exit while loop if username is unique

    password = input("Enter a new password: ")
    user_info = f"{username}:{password}\n"

    with open('user_database.txt', 'a+') as f:
        f.write(user_info)
        print("Successfully created account! Welcome to MBMH.")
        sys.exit()

# Context Manager method of opening files, no need to close the file
# a+ mode to append and read

def validate_credentials(username, password, user_data):
    for user, stored_password, in user_data:
        if username == user and password == stored_password:
                return True
    return False


def log_user_in():
    max_attempts = 3
    while max_attempts >0:
        username = input("Welcome back! Please enter your username: ")
        password = input(f"Please enter your password (Attempts Remaining: {max_attempts}): ")

        with open('user_database.txt', 'r') as f:
            user_data = [line.strip().split(':') for line in f]
            # List comprehension - compresses the code and inserts it into a list, separating user and password
            if validate_credentials(username, password, user_data):
                print("Logged in successfully! \u2713\n")

                change = input("Would you like to change your password? (y/n): ")
                if change == 'y':
                    new_pass = input("Enter your new password: ")

                    for i, (user, stored_pass) in enumerate(user_data):
                        # Use of enumerate keyword to both iterate and keep track of iteration number
                        if username == user:
                            user_data[i] = (user, new_pass)
                            with open('user_database.txt', 'w') as f:
                                for user, stored_pass in user_data:
                                    f.write(f"{user}:{stored_pass}\n")
                            print("Successfully updated password.")
                else:
                    sys.exit()


def main():
    print("Welcome to MBMH Interface!")
    while True:
        option = input("Logging in? Signing up?\nPlease select an option (L/S): ")
        if option == 'S':
            register_user()
        elif option == 'L':
            if log_user_in():
                # If log_user_in() == True, then break
                break
        else:
            print("Please enter valid input. Redirecting...")
            time.sleep(2)

main()
