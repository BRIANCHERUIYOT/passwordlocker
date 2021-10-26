import unittest
from locker import User
class Testuser(unittest.TestCase):
    '''
    class testing the User functionality
    '''
    # print("hello")
    def setUp(self):
        '''
        create a test for friend credenntials
        '''
        self.new_user - User ("Brian","1234@345ghjk")
        
    # print("hello")

        
    def test(self):
        self.assertEqual(self.new_user.user_name,"Brian")
        self.assertEqual(self.new_user.password,"1234@345ghjk")
        
    # print("hello")
if __name__ == "__main__":
    unittest.main(Testuser)
