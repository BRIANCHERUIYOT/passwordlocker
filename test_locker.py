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


  
        
    print("hello")
if __name__ == "__main__":
    unittest.main()
