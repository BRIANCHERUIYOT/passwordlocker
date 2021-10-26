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
        
        
        
class Credential:
    """
    Class that generates instances of credential
    """

    credential_list =[]


    def __init__(self, account, acnt_username, acnt_password):
        self.account = account
        self.acnt_username = acnt_username
        self.acnt_password = acnt_password

    def save_credential(self):
        '''
        save user objects into credential
        ''' 
        Credential.credential_list.append(self)   

    def delete_credential(self):
        '''
        deleteletes saved contact
        '''
        Credential.credential_list.remove(self)

    def test_save_credential(self):
        pass

   
        