class Queuewatch():
    def __init__(self):
        self.__placeid = 0
        self.__placename = "test"
        self.__watchurl = "https://polyclinic.singhealth.com.sg/patient-care/Pages/Qwatch.aspx"
        self.__currentqueue = 0
        self.__estwaitingtime = 0