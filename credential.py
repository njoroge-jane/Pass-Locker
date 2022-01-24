class Credential:

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

        Credential.credential_list.append(self)  

    def delete_credential(self):

        Credential.credential_list.remove(self)  

@classmethod
def find_by_account(cls,account):    
     for credential in cls.credential_list:
            if credential.account == account:
                return credential               