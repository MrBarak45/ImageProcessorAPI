from API.User import User
from API.Client import Client
from API.Authenticator import Authenticator
import time
from datetime import datetime


if __name__ == '__main__':
    testUser = User("pkettmus@gmail.fr", "azezrty1234")
    client = Client(testUser, Authenticator('http://23.102.34.223:8080/login'))

    while True:
        now = datetime.now()
        print('========================================================')
        print("New iteration: " + now.strftime("%d/%m/%Y %H:%M:%S"))
        client.Start()
        time.sleep(40)
