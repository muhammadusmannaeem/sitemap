'''
the server IP address, username and password can be hardcoded or read from a file depending on how maintainers see fit.
'''

'''
 Uploads a file on server using FTP
 Args:
     targetpath: the ftp path where the file is to be uploaded.
     filepath: the config file path
 Returns:
     None
 Raises:
     None.
 '''


import os
from src/_config.py import get_config
import ftplib

def uploadFile(targetpath, filepath):
    server = get_config("server")
    username = get_config("username")
    password = get_config("password")
    ftp = ftplib.FTP(server, username, password)
    if(os.path.isfile(filepath)):
        ffile = open(filepath, 'rb')
        ftp.storbinary('STOR %s' % targetpath, ffile)
        ffile.close()
    else:
        print ("Please check your path correctly")
