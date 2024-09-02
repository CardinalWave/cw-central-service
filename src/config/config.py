import configparser
import os


class Config:
    config = configparser.ConfigParser()
    config.read('src/config/config.ini')

    CW_AUTH_SERVICE = config['CW_AUTH_SERVICE']['BaseURL']

    CW_LOG_TRACE = config['CW_LOG_TRACE']['BaseURL']
    CW_LOG_TRACE_IP = config['CW_LOG_TRACE']['IP']
    CW_LOG_TRACE_PORT = config['CW_LOG_TRACE']['PORT']

    CW_CENTRAL_SERVICE = config['CW_CENTRAL_SERVICE']['SERVICE']
    CW_CENTRAL_SERVICE_IP = config['CW_CENTRAL_SERVICE']['IP']
    CW_CENTRAL_SERVICE_PORT = config['CW_CENTRAL_SERVICE']['PORT']
    CW_CENTRAL_SERVICE_URL = config['CW_CENTRAL_SERVICE']['BaseURL']

    # # From Dockerfile
    CW_AUTH_SERVICE = os.getenv('CW_AUTH_SERVICE', CW_AUTH_SERVICE)
