import configparser

from utilities.files_utils import FilesUtils
from utilities.xml_utils import XmlUtils
from utilities.xls_utils import XlsUtils

config = configparser.ConfigParser()
config.read('config.ini')

ZIP_FOLDER = config['DEFAULT']['ZIP_FOLDER']
XML_FOLDER = config['DEFAULT']['XML_FOLDER']
XLS_FOLDER = config['DEFAULT']['XLS_FOLDER']

FilesUtils.unzip(ZIP_FOLDER + "\SwiftNess_015968100_201803201913.zip" ,XML_FOLDER)
member = XmlUtils.parse_folder_to_member(XML_FOLDER)
XlsUtils.export(member,XLS_FOLDER + "/test_akiva.xlsx")