import sqlite3


class Config:
    def __init__(self):
        self.__google_api_key = "0"

    def get_api_key(self):
        return self.__google_api_key

    def read_file(self):
        try:
            api_key = open("google_maps_api_key.txt","r")
            return api_key.readline()
        except:
            return "API_txt_not_found"

    def set_api_key(self):
        self.__google_api_key = self.read_file()

    def database_connection(self):
        return sqlite3.connect("../site.db")
