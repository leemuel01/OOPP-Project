import datetime

class Feedback():

    def __init__ (self, subject, content):
        self.__subject = subject
        self.__content = content
        self.__date = datetime.datetime.now()
        self.__wordcount = len(self.__content.split())


###########Accessors#################


    def get_subject (self):
        return self.__subject

    def get_content (self):
        return self.__content

    def get_date (self):
        return self.__date

    def get_wordcount (self):
        return self.__wordcount

#############Mutators###############

    def set_subject (self,subject):
        self.__subject=subject

    def set_content (self,content):
        self.__content = content

    def set_date (self,date):
        self.__date = date

    def set_wordcount (self,wordcount):
        self.__wordcount=wordcount


# form=feedback("joe","the lazy fox jumped into a ditch")
# print(form.get_date())
# print(form.get_wordcount())