from entities.member_personal_data import MemberPersonalData
from entities.mutzar import Mutzar
from utilities.printable import Printable

class Member(Printable):

    def __init__(self):

        self.__mutzarim = []
        self.member_personal_data = None
    

    @property
    def member_personal_data(self):

        return self.__member_personal_data

    # The setter for the chain property
    @member_personal_data.setter 
    def member_personal_data(self, val):

            self.__member_personal_data = val


    def add_mutzar(self,mutzar):

        self.__mutzarim.append(mutzar)

    
    def get_mutzarim(self):

        return self.__mutzarim[:]