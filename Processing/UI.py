from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from API.User import User
from API.Client import Client
from API.Authenticator import Authenticator
import time
from datetime import datetime
#from DBMS_Project import *


class Authentication:

    def __init__(self, root):

        self.root = root
        self.root.title('Picturization Login')

        '''Make Window 10X10'''

        rows = 0
        while rows < 10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1

        '''Username and Password'''
        frame = LabelFrame(self.root, text='Login')
        frame.grid(row=1, column=1, columnspan=10, rowspan=10)

        Label(frame, text=' Username ').grid(row=2, column=1, sticky=W)
        self.username = Entry(frame)
        self.username.grid(row=2, column=2)

        Label(frame, text=' Password ').grid(row=5, column=1, sticky=W)
        self.password = Entry(frame, show='*')
        self.password.grid(row=5, column=2)

        # Button
        ttk.Button(frame, text='LOGIN', command=self.login_user).grid(row=7, column=2)

        '''Message Display'''
        self.message = Label(text='', fg='Red')
        self.message.grid(row=9, column=6)

    def login_user(self):
        user = User(self.username.get(), self.password.get())
        authenticator = Authenticator('http://23.102.34.223:8080/login')
        token = ''
        try:
            token = authenticator.AuthenticateUser(user)
        except:
            print("Invalid Username/password")

        '''Check username and password entered are correct'''
        if token != '':
            # Destroy current window
            root.destroy()

            # Open new window
            newroot = Tk()
            client = Client(user, authenticator=authenticator)
            while True:
                now = datetime.now()
                print('========================================================')
                print("New iteration at: " + now.strftime("%d/%m/%Y %H:%M:%S"))
                client.Start()
                time.sleep(40)
            #application = School_Portal(newroot)
            newroot.mainloop()
            #todo add a screen for logout and loading timer


        else:
            '''Prompt user that either login or password is wrong'''
            self.message['text'] = 'Username or Password incorrect. Try again!'



if __name__ == '__main__':
    root = Tk()
    root.geometry('425x185+700+300')
    application = Authentication(root)

    root.mainloop()