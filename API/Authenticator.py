import requests





class Authenticator:

    LOGIN_ENDPOINT = ''
    CURRENT_TOKEN = ''

    def __init__(self, login_endpoint):
        self.LOGIN_ENDPOINT = login_endpoint


    def AuthenticateUser(self, user):
        payload = {"email": user.Email, "password": user.Password}
        jsonResponse = requests.post(self.LOGIN_ENDPOINT, json=payload).json()
        self.CURRENT_TOKEN = jsonResponse["token"]
        return self.CURRENT_TOKEN







