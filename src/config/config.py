import configparser
import os

class Config:
    config = configparser.ConfigParser()
    config.read('src/config/config.ini')

    CW_AUTH_SERVICE = config['CW_AUTH_SERVICE']['BaseURL']
