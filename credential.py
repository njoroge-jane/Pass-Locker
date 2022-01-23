class Credential:
    """
    Class that stores existing user credentials.
    """

    credential_list = [] 

    def __init__(self,account,user_name,password):

        '''
        Args:
            account: New credential account.
            user_name : New credential user name.
            password: New credential password.
        '''

        self.account = account
        self.user_name = user_name
        self.password = password
  
    def save_credential(self):

        '''
        save_credential method saves contact objects into credential_list
        '''

        Credential.credential_list.append(self)  