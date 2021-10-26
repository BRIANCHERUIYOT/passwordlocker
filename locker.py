class User:
    '''
    class generates new instance of user 
    '''
    user_list=[]
    def _init_user(self,user_name,password):
        self.user_name=user_name
        self.password=password
    def save_user(self):
        '''
        save user method saves a new user objects to the user user_list  
        '''  
        User.user_list.append(self)