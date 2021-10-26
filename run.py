from locker import User, Credential
import getpass


def create_user(name, password):
    """
    Parameters
    """
    created_user = User(name, password)
    return created_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()
    
def delete_user(user):
    """
    delete user function
    """
    user.delete_user()
    
    
def create_credential(account, acnt_username, acnt_password):
    """
    Parameters
    """
    new_credential = Credential(account, acnt_username, acnt_password)
    return new_credential

def save_credential(credential):
    """
    Function to save credential
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete credential
    """
    credential.delete_credential()


def find_credential(acnt_username):
    """
    Function to find credential
    """
    return Credential.find_by_acnt_username(acnt_username)


def check_existing_credentials(acnt_username):
    """
    Function to check existing credential
    ----------
    name
    Returns
    -------
    user
    """
    return Credential.find_by_acnt_username(acnt_username)


def display_credentials():
    """
    Function to display credential
    Returns
    -------
    """
    return Credential.display_all_credentials()

def main():
    
    user_name = input("Enter your name > ")
    print(f"Hi {user_name}, WELCOME!!!!") 
    a_member= input(f"{user_name}.Already a member? YES/N0 > ").lower()

    if a_member == "no":
        print("Wow singnup with us!")
        user_name = input("Please Enter your preferred username..> ")

        p_generate = input(f"{user_name}. Can we  generate password for you? YES/N0 > ").lower()
        if p_generate == "no":
            print("-"*30)
            print("|Password saved and secure.|")
            print("-"*30)
            getpass.getpass()
            print("PERFECT!! YOU ARE NOW LOGGED IN")

        while True:
            print("""
            USE THE SHORT ABBREVIATION
            cc - to create a new credential
            dc - to display credential
            fc - to find credential
            xx - to delete credential
            rp - random password
            """)
           

    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
     main()