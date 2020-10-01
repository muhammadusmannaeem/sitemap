'''
targetpath: the ftp path where the file is to be uploaded.
filepath: the config file path
the server IP address, username and password can be hardcoded or read from a file depending on how maintainers see fit. 
'''


import os
import ftplib

def uploadFile(targetpath, filepath):
    ftp= ftplib.FTP(server, username, password)
    if(os.path.isfile(filepath)):
        ffile= open(filepath, 'rb')
        ftp.storbinary('STOR %s' % targetpath, ffile)
        ffile.close()
    else:
        print ("Please check your path correctly")