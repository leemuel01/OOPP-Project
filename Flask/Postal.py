#test

class Postalcode():
    def __init__(self,postalcode):
        self.__postalarea=int(str(postalcode)[0:2])  # cant manipulate without converting#
        self.__location_dict={

        }
        for i in range(1,7):  # 1 to 6
            self.__location_dict[i]="Raffles Place, Cecil, Marina, Peoples Park"
        for i in range(7,9):
            self.__location_dict[i]="Anson, Tanjong Pagar"
        for i in range(9,11):
            self.__location_dict[i]="Telok Blangah, Harbourfront"


    def getpostalarea(self):
        return self.__postalarea

    def generallocation(self):
        if (self.__postalarea <= 0):
            return 'Error'
        elif (self.__postalarea <=6):
            return 'Raffles Place, Cecil, Marina, Peoples Park'
        elif (self.__postalarea <=8):
            return 'Anson, Tanjong Pagar'
        elif (self.__postalarea <=10):
            return 'Telok Blangah, Harbourfront'
        elif (self.__postalarea <=13):
            return 'Pasir Panjang, Hong Leong Garden, Clementi New Town'
        elif (self.__postalarea <=16):
            return 'Bukit Merah, Queenstown, Tiong Bahru'
        elif (self.__postalarea <=17):
            return 'High Street, Beach Road'
        elif (self.__postalarea <=19):
            return 'Middle Road, Golden Mile'
        elif (self.__postalarea <=21):
            return 'Little India, Farrer Park, Jalan Besar, Lavender'
        elif (self.__postalarea <=23):
            return 'Orchard, Cairnhill, River Valley'
        elif (self.__postalarea <=27):
            return 'Ardmore, Bukit Timah, Holland Road, Tanglin'
        elif (self.__postalarea <=30):
            return 'Watten Estate, Novena, Thomson'
        elif (self.__postalarea <=33):
            return 'Balestier, Toa Payoh, Serangoon'
        elif (self.__postalarea <=37):
            return 'Macpherson, Braddell'
        elif (self.__postalarea <=41):
            return 'Geylang, Eunos'
        elif (self.__postalarea <=45):
            return 'Katong, Joo Chiat, Amber Road'
        elif (self.__postalarea <=48):
            return 'Bedok, Upper East Coast, Eastwood, Kew Drive'
        elif (self.__postalarea <=50):
            return 'Loyang, Changi'
        elif (self.__postalarea <=52):
            return 'Simei, Tampines, Pasir Ris'
        elif (self.__postalarea <=55):
            return 'Serangoon Garden, Hougang, Punggol'
        elif (self.__postalarea <=57):
            return 'Bishan, Ang Mo Kio'
        elif (self.__postalarea <=59):
            return 'Upper Bukit Timah, Clementi Park, Ulu Pandan'
        elif (self.__postalarea <=64):
            return 'Jurong, Tuas'
        elif (self.__postalarea <=68):
            return 'Hillview, Dairy Farm, Bukit Panjang, Choa Chu Kang'
        elif (self.__postalarea <=71):
            return 'Lim Chu Kang, Tengah'
        elif (self.__postalarea <=73):
            return 'Kranji, Woodgrove, Woodlands'
        elif (self.__postalarea <=74):
            return 'None'
        elif (self.__postalarea <=76):
            return 'Yishun, Sembawang'
        elif (self.__postalarea <=78):
            return 'Upper Thomson, Springleaf'
        elif (self.__postalarea <=80):
            return 'Seletar'
        elif (self.__postalarea <=81):
            return 'Loyang, Changi'
        elif (self.__postalarea <=82):
            return 'Serangoon Garden, Hougang, Punggol'
        else:
            return 'Error'

    def getnearbyclinictest(self):
        if self.__postalarea < 50:
            return ''
        else:
            return ''


test=Postalcode(6)
print(test.getpostalarea())
print(test.generallocation())