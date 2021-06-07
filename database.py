#this file is going to server as our data base
# where we would be going through our files

#CRUD

#create record 
#update record
#read record
#delete record
#find user based on account number


def create(account_number, user_detail):
    print("Create a new user record")
    try:
        f = open("data/user_record/" + str(account_number) + ".txt", "x")
        f.write(user_detail)
    except FileExistsError:
        print('File already exist')
        #delete the already created file, and print out error, then return false
        update()
    finally:
        f.close()

    # create a fie
    # name of the file would be account_number.txt
    # add the user details to the file
    # if saving to file fails then delete selected files


def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file 
    # update the content of the file
    # save the file
  


def read(user_account_number):
    print("read user record")
    # find user with account number
    # ftech content of the file



def delete(user_account_number):
    print("delete user record") 
    #find the user with account number
    #delete the user record (file)
    #return true



def find(user_account_number):
    print("find user")

create(333, 'tomi')