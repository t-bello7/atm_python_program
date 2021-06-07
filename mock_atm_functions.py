#register 
#- first_name,last_name, password ,email
#- generating user account

#login by email or account number and password

#banking option

#basic login to your atm profile

#initializing the system

import random
import database
import auth



# We want to update our database to files
database = {
    9748182824: ['bello4aus@gmail.com','tomi', 'bello', 'password', 0],
    3267360064: ['benNjoku@gmail.com','bem', 'Njoku', 'password',0]
} #dictionay

def init():
    is_valid_option_selected = False
    print('Welcome to bank PHP ')

    while is_valid_option_selected == False:
        haveAccount = int(input("Do you have account with us (1) Yes or 2(No)s \n-->"))

        if haveAccount ==1 :
            is_valid_option_selected = True
            login()
        elif haveAccount == 2 :
            is_valid_option_selected = True
            print(register())
        else:
            print("You have selected invalid option")

def login():
    print("******* Login *******")
    account_number_from_user = input("What is your account number? \n-->")
    is_valid_account_number = auth.account_number_validation(account_number_from_user)
    if is_valid_account_number:
        password = input("What is your password \n--> ")   
        # account number is the key , user_details is the value -- E choke me small that is why im commenting it
        for account_number,user_details in database.items():
            if account_number == int(account_number_from_user) in database:
                if user_details[3] == password:
                    bank_operation(user_details)
    else:
        init()
    
    


def password_validation(password):
    #learn regex young man for date email ,stron password and other things
    pass

def register():
    print("****User registration*******")
    email = input("What is your email address ? \n -->")
    first_name =input("What is your first name \n -->")
    last_name = input("What is your last name \n -->")
    password = input('Create password \n -->')

    account_number =generate_account_number()

    database[account_number] = [first_name,last_name, password]
    print('Your account has been created')
    print(" === ==== ==== === ==== ==")
    print("Your account Number is %d"% account_number)
    print("Make sure you keep it safe")
    print("=== ==== ======== ===== ==")
    
    login()
    

def bank_operation(user):
    print("Welcome %s %s "%(user[0],user[1]))
    selected_option = int(input("What would you like to do?\n (1) Deposit \n (2)Withdrawal \n (3) Logout \n (4) Exit \n -->"))
    if (selected_option == 1):
        deposit_operation(user)
    elif(selected_option == 2):
        withdrawal_option(user)
    elif(selected_option == 3):
        logout()
    elif(selected_option == 4):
        exit()
    else:
        print("You have selected invalid option")
        init()

def deposit_operation(user):
    balance = get_current_balance(user)
    deposit = int(input('How much do you want to deposit? \n -->'))
    balance += deposit

    print("=== ====== =========")
    print('You current balance is now %s .\n..Rember to add update your database'%deposit)
    print("=== ===== ===== ===")
    bank_operation(user)

def withdrawal_option(user):
    #get current balance 
    #get amount to withdraw
    #check if current balance > withdraw balance
    #deduct withdrawn amount from current balance
    #display current balance
    balance = get_current_balance(user)
    withdrawal = int(input('How much do you want to withdraw ?'))
    if withdrawal < balance :
        print("===== ======== ===")
        print('Cash out king .You have succesfully withdrawn %s \n'%swithdrawal)
        balance -= withdrawal
        print('Your balance is now %s.... Remeber to update your database ' %balance)
        print("=== ======= ======= ===")
    else:
        print('You have insufficient Funds')

        bank_operation(user)

def get_current_balance(user_details):
    return user_details[4]

def generate_account_number():
    return random.randrange(1111111111,9999999999)

def logout():
    login()
### Actual Banking System ###
init()
