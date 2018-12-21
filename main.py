import configparser

from utilities.files_utils import FilesUtils
from utilities.xml_utils import XmlUtils

config = configparser.ConfigParser()
config.read('config.ini')

ZIP_FOLDER = config['DEFAULT']['ZIP_FOLDER']
XML_FOLDER = config['DEFAULT']['XML_FOLDER']

FilesUtils.unzip(ZIP_FOLDER + "\SwiftNess_015968100_201803201913.zip" ,XML_FOLDER)
XmlUtils.parse_folder_to_member(XML_FOLDER)