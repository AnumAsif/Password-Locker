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

    def test_save_multiple_credential(self):
        '''
        test case to check if we can save multiple credential objects to the credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("anum","Instagram","anumasif","fdsf134csd")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_check_user(self):
        '''
        test case to check if the user exists
        '''
        self.new_user.save_user()
        test_user= User("sana","sana12345")
        test_user.save_user()
        self.assertEqual(test_user.username,"sana")

    def test_delete_credential(self):
        '''
        test case to check if an unwanted credential is deleted
        '''
        self.new_credential.save_credential()
        test_credential = Credential("anum","Instagram","anumasif","fdsf134csd")
        test_credential.save_credential()
        test_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_generate_password(self):
        '''
        test case to check if the password is generated
        '''
        self.assertTrue(Credential.generate_password())

    def test_find_credential(self):
        '''
        test case to find credential of a particular site
        '''
        self.new_credential.save_credential()
        test_credential = Credential("anum","Instagram","anumasif","fdsf134csd")
        test_credential.save_credential()
        self.assertEqual(Credential.find_credential("Instagram"),test_credential)

    def test_credential_exist(self):
        '''
        test case to check if the credential exists
        '''
        self.new_credential.save_credential()
        test_credential = Credential("anum","Instagram","anumasif","fdsf134csd")
        test_credential.save_credential()
        self.assertTrue(Credential.credential_exist("Instagram"))

    def test_display_credentials(self):
        '''
        test case to check if the function return the credential list of user
        '''
        self.new_credential.save_credential()
        test_credential = Credential("anum","Instagram","anumasif","fdsf134csd")
        test_credential.save_credential()
        self.assertEqual(len(Credential.display_credentials("anum")),2)



if __name__ == '__main__':
    unittest.main()
