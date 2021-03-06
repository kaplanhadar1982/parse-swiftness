import xml.etree.ElementTree as ET
import os

from entities.member import Member
from entities.mutzar import Mutzar
from entities.maasik import Maasik
from entities.member_personal_data import MemberPersonalData

class XmlUtils:


    @classmethod
    def parse_folder_to_member(cls,folder_name):

        member = Member()

        for filename in os.listdir(folder_name):
            if filename[-4:] == '.xml' :
                cls.parse_one_xml(member,folder_name+'\\'+filename)
        
        print(member)
        return member
        


    @classmethod
    def parse_one_xml(cls,member,filename):

        tree = ET.parse(filename)
        root = tree.getroot()

        #fill pesonal data only if not exists
        if member.member_personal_data == None :
            member.member_personal_data = MemberPersonalData(
                cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/NetuneiMutzar/YeshutLakoach/MISPAR-ZIHUY-LAKOACH'),
                cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/NetuneiMutzar/YeshutLakoach/SHEM-PRATI'),
                cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/NetuneiMutzar/YeshutLakoach/SHEM-MISHPACHA'),
                cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/NetuneiMutzar/YeshutLakoach/TAARICH-LEYDA'))

        mutzar = Mutzar(
            cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/NetuneiMutzar/SUG-MUTZAR'),
            cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/HeshbonotOPolisot/HeshbonOPolisa/SHEM-TOCHNIT'),
            cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/HeshbonotOPolisot/HeshbonOPolisa/PirteiTaktziv/PerutMasluleiHashkaa/SHEM-MASLUL-HASHKAA'),
            cls.read_one_cell(root,'./YeshutYatzran/Mutzarim/Mutzar/HeshbonotOPolisot/HeshbonOPolisa/TAARICH-HITZTARFUT-MUTZAR'))

        for f_maasik in root.findall('./YeshutYatzran/Mutzarim/Mutzar/NetuneiMutzar/YeshutMaasik'):
            maasik = Maasik(f_maasik.find('SHEM-MAASIK').text)
            mutzar.add_maasik(maasik)

        member.add_mutzar(mutzar)

    @staticmethod
    def read_one_cell(root,cell):
        try:
            return root.find(cell).text.strip()
        except:
            return ''
