
import datetime as datetime

class Student:
    __name = ""
    __gender = ""
    __adminnum = ""
    __mark = 0.0
    __date = datetime.datetime.now()

    def __init__(self, name, gender, adminnum):

        # if not name.isalpha():
        #     raise ValueError("Not a valid name")
        #
        # if gender.capitalize() not in ["Male", "Female"]:
        #     raise ValueError("Not a valid gender")
        #
        # if len(adminnum) != 7 or not adminnum[-1].isalpha():
        #     raise ValueError("Not a valid Admin number")

        ##### Need to define #####
        self.__name = name
        self.__gender = gender
        self.__adminnum = adminnum

        ##### Defined values #####

        self.__mark = 0.0
        self.__date = datetime.datetime.now()

############### Setting Methods #####################

    def set_date(self, date):
        self.__date = date

    def set_mark(self, mark):
        self.__mark = mark

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

################  Getting Methods  #####################

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_mark(self):
        return self.__mark

    def get_adminnum(self):
        return self.__adminnum

    def get_date(self):
        return self.__date

##### What happens when you print the student #####

    def __str__(self):
        s = f"Name: {self.get_name()}\nGender: {self.get_gender()} \nMarks: {self.get_mark()} \nAdmin Number: {self.get_adminnum()} \nEnrollment Date: {self.get_date()}"
        return s

#############################################

s1 = Student("Lemuel", "Male", "182125A")
s1.set_mark(100)
print(s1)