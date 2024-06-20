
def email_exists (email, filename='database/accounts.txt'):
    accounts_file = open(filename, 'r')
    for line in accounts_file:
        parts = line.strip().split(",")
        email_check = parts[0]

        if email_check == email:
            return True
        
    return False

    

def create_new_account ():
    email = input ("Enter your email: ")
    password = input ("Create a password: ")

    if email_exists(email):
        print (f"Error: The email {email} is already registered.")
    else:
        accounts_file = open('database/accounts.txt', 'a')
        info = f"{email},{password}\n"
        accounts_file.writelines(info)
        print ("Account Created Successfully!")
        accounts_file.close()



def login_to_account ():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email_exists(email) == False:
        print("Email or password incorrect. Please try again.")
        return False

    accounts_file = open('database/accounts.txt', 'r')
    for line in accounts_file:
        parts = line.strip().split(",")
        email_check = parts[0]
        password_check = parts[1]

    if email_check == email and password_check == password:
        print("Logged in successfully!")
        accounts_file.close()
        return True
    
    accounts_file.close()

    print("Email or password incorrect. Please try again.")
    return False
        


def main():
    while True:
        print("----------FitCheck----------")
        print()
        print("1. Create an account")
        print("2. Login to account") 
        print("3: Quit")
        print()
        print("----------FitCheck----------")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            create_new_account()
        elif choice == '2':
            login_to_account()
            break
        elif choice == '3': 
            break
        else:
            print("Invalid choice, please try again.")



if __name__ == '__main__':
    main()
