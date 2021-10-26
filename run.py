from locker import User



def create_user(name, user_password):
    """
    Parameters
    """
    created_user = User(name, user_password)
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