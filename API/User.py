#Test class for authentication of user
class User:
    Email = ''
    Password = ''

    USEREMAIL = ''

    def __init__(self, email, password):
        self.Email = email
        self.Password = password
        self.USEREMAIL = email
