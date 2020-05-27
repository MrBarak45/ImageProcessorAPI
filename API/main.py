from API.User import User
from API.Client import Client
from API.Authenticator import Authenticator

if __name__ == '__main__':
    testUser = User("pkettmus@gmail.fr", "azezrty1234")
    client = Client(testUser, Authenticator('http://23.102.34.223:8080/login'))
    client.Start()
