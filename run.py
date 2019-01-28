#!/usr/bin/env python3.6
from user import User, Credential
def create_user(username,password):
    """
    Function to create a new user
    """
    new_user=User(username,password)
    return new_user
def save_user(user):
    """
    Function to save created user
    """
    User.save_user(user)
def check_user(username, password):
    """
    Function to check if the user with the given username and password exists
    """
    return User.check_user(username, password)
def create_credential(username,sitename,accountname,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(username, sitename, accountname, password)
    return new_credential
def save_credential(credential):
    """
    Function to save new credential
    """
    Credential.save_credential(credential)

def del_credential(credential):
    """
    Function to delete a credential
    """
    Credential.delete_credential(credential)
def generate_password():
    """
    Function to generate a password for new account
    """
    return Credential.generate_password()
def find_credential(site_name):
    """
    Function that finds a credential info of an account by company name
    """
    return Credential.find_credential(site_name)
def check_existing_credential(site_name):
    """
    Function that checks if a credential info of an account exists and return a Boolean
    """
    return Credential.credential_exist(site_name)

def display_credentials(user_name):
    """
    Function that returns all the saved credentials
    """
    return Credential.display_credentials(user_name)




            #     print("{{name}}, welcome to your account. What would you like to do")
            #     accountFor = input("Enter name for which you want to save your credential")
            #     accountUsername = input("Enter user name for the account")
            #     print("Do you want to autogenerate password. If yes, press 'Y' else press 'N'")
            #     while True:
            #         answer = input().lower();
            #         if answer == 'y':
            #             accountPassword = random.randint(100000,200000)
            #             break
            #         elif answer == 'n':
            #             print("Enter the password for the account:")
            #             accountPassword = input()
            #             break
            #         else:
            #             print("Unable to understand. Type again")
            #     save_credential(new_user)
            #     new_credential = credentials(accountFor, accountUsername, accountPassword)
            #     new_user.credential_list.append(new_credential)
            # else:
            #     print("user for whom you want to save credentials doesnot exist")
        # if short_code == "dc":
        #     name =input("Enter your username")
        #     password = print ("Enter your password")
        #     if name == new_user.name and password == new_user.password:
if __name__ == '__main__':
    main()
