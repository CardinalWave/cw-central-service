import configparser
import os


class Config:
    config = configparser.ConfigParser()
    config.read('src/config/config.ini')

    CW_AUTH_SERVICE = config['CW_AUTH_SERVICE']['BaseURL']

    CW_LOG_TRACE = config['CW_LOG_TRACE']['BaseURL']
    CW_LOG_TRACE_IP = config['CW_LOG_TRACE']['IP']
    CW_LOG_TRACE_PORT = config['CW_LOG_TRACE']['PORT']

    # # From Dockerfile
    CW_AUTH_SERVICE = os.getenv('CW_AUTH_SERVICE', CW_AUTH_SERVICE)
