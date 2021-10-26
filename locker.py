class User:
    """
    Class that generates new instances of Users
    """
    user_list = []

    def __init__(self, user_name, password):
        self.name = user_name
        self.password= password


    def delete_user(self):
        """
        delete_user method deletes saved contact
        """
        User.user_list.remove(self)      
        
        
    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

   
        