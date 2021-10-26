import unittest
from locker import User

class TestUser(unittest.TestCase):
    """
        Test class that defines test cases for the user class behaviours.
    """

    def setUp(self):
        self.created_user = User("Brian", "1234@345ghjk")


    def tearDown(self):
        User.user_list = []


    def test_init(self):
        self.assertEqual(self.created_user.name, "Brian")
        self.assertEqual(self.created_user.password, "1234@345ghjk")
        
        
    def test_delete_user(self):
        """
          test_delete_user to test if we can remove a user from our users list
        """
        self.created_user.save_user()
        test_user = User("Brian", "1234@345ghjk")
        test_user.save_user()

        self.created_user.delete_user()
        self.assertEqual(len(User.user_list), 1)


  
        
    print("hello")
if __name__ == "__main__":
    unittest.main()
