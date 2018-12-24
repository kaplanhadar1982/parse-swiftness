from utilities.printable import Printable

class Mutzar(Printable):


    def __init__(self,sug_mutzar,shem_tochnit,
                 shem_maslul_hashkaa,hitztarfut_date):

        self.sug_mutzar = sug_mutzar
        self.shem_tochnit = shem_tochnit
        self.shem_maslul_hashkaa = shem_maslul_hashkaa
        self.hitztarfut_date = hitztarfut_date
        self.__maasikim = []
    
    @property
    def hitztarfut_date(self):
        
        return self.__hitztarfut_date[-2:] + '/' + self.__hitztarfut_date[4:6] + '/' + self.__hitztarfut_date[:4]


    @hitztarfut_date.setter 
    def hitztarfut_date(self, val):

        self.__hitztarfut_date = val


    def add_maasik(self,maasik):

        self.__maasikim.append(maasik)

    
    def get_maasikim(self):

        return self.__maasikim[:]