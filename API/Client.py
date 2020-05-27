import requests

class Client:

    _user = []
    _authenticator = []

    def __init__(self, user, authenticator):
        self._user = user
        self._authenticator = authenticator

    def Start(self):
        tokenJson = self._authenticator.AuthenticateUser(self._user)
        print(tokenJson + '\n')

        url = 'http://23.102.34.223:8080/images/untreated'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self._authenticator.CURRENT_TOKEN}

        j = requests.get(url, headers=headers)
        print(j.text)
