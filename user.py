# from credentials import Credentials
import random
class User:
    """
    Class that generates new instances of User
    """

    user_list = []
    # credentials_list=[]
    def __init__(self,username,password):
        '''
        __init__ method helps us define properties for our objects.

        Args:
            username: New user's username.
            password : New user's password.
            credentials[]:An array containing credential information of a user accounts
        '''
        self.username = username
        self.password = password
    def save_user(self):
        """
        save_user method saves a user in user_list[]
        """
        User.user_list.append(self)
    @classmethod
    def check_user(cls, username, password):
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user.username
