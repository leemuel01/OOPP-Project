import datetime

class User():

    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email

        self.__date_registered = datetime.datetime.now().date()

        self.__badges = []
        self.__messages = []
        self.__medical_history = []

#=================Accessors=================#

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_date_registered(self):
        return self.__date_registered

    def get_badges(self):
        return self.__badges

    def get_messages(self):
        return self.__messages

    def get_medical_history(self):
        return self.__medical_history

#==================Mutators=====================#

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def set_badges(self, badge):
        self.__badges.append(badge)

    


user = User("test", "test", "test")
print(user.get_date_registered())

