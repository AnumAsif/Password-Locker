import unittest
from user import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class and credential class
    Args:
        unittest.TestCase: Class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Method to run before each test case
        '''
        self.new_user = User("anum","anum12345")
        self.new_credential = Credential("anum","Google","anumasif","anum12345")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        Credential.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"anum")
        self.assertEqual(self.new_user.password,"anum12345")
        self.assertEqual(self.new_credential.user_name,"anum")
        self.assertEqual(self.new_credential.site_name,"Google")
        self.assertEqual(self.new_credential.account_name,"anumasif")
        self.assertEqual(self.new_credential.account_password,"anum12345")

    def test_save_user(self):
        '''
        test case to test if the user object is saved to the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_credential(self):
        '''
        test case to test if the credential object is saved in the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    


if __name__ == '__main__':
    unittest.main()
