from utilities.printable import Printable

class MemberPersonalData(Printable):


    def __init__(self,identity_number,first_name,
                 last_name, birth_date):

        self.identity_number = identity_number
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date


    @property
    def birth_date(self):
        
        return self.__birth_date[-2:] + '/' + self.__birth_date[4:6] + '/' + self.__birth_date[:4]


    @birth_date.setter 
    def birth_date(self, val):

        self.__birth_date = val

    @property
    def identity_number(self):
        
        return self.__identity_number[-9:]


    @identity_number.setter 
    def identity_number(self, val):

        self.__identity_number = val