def account_number_validation(account_number):
    # checkif account number is not empty
    # if the account number is 10 digits
    # if the account number is an integer
    if account_number:
        if len(str(account_number)) == 10:
            #best way to check if account number is an integer is to convert it to integer again

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account number, account number shoulc be an integer")
                return False
            except TypeError:
                print("Invalid Account Type")
                return False

        else:
            print("Account Number cannot be more than  or less than 10 digits")
            return False
    else:
        print("Account Number is a required Field")
        return False