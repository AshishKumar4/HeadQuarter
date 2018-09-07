#!/usr/bin/python
# Author: WhiteOracle
# Main Command and Control Center
#   Fires up the temporary and permanent listeners as well as sets up the stagers,
#   injects temporary and permanent backdoors into the targets and
#   Also sets up persistant backdoors. 
#  There are two types of backdoors -> 
#       Primary Backdoors, the active backdoor for fast access; Usually Pty based.
#       Secondary Backdoors, for persistance; used to inject primary backdoor in every session

# TODO: 
# Standardize all backdoors, make them print 'Success' or Failure' messages so we know if them worked or not.
# Also implement other checks too like timeout etc.

# Basic Layout -->
#   1. Give option to connect to remote shell, bind or reverse
#   2. connect to the ip:port, give option to interact or inject persistance modules or other backdoor, also, Available Sessions
#   3. for inject backdoor ->
#       3.1 List all available backdoors in the directoy
#       3.2 send command to remote to download selected backdoor from host and Run it. Verify the output for Success or Failure
#   4. For inject Persistance ->
#       4.1 List persistance backdoor modules
#       4.2 download a derivative of flinux there and create scripts to start backdoors on bootup.
#       4.3 run backdoor and verify if working.

#   For Every Persistant Backdoor, Code should be generated to bypass dynamic IP problems, as well as 
#   Uniquely assigned port numbers, with a database of pwned servers, basically as json file.

# For Every backdoor, read the file contents, replace "XX.YY.ZZ.OO" with Local Host IP (if reverse shell) and Port 42841 with port,
# Encode the string, save it to dynamically generated randomly named file on local server (this), send command to remote to
# Download this file, and execute it according to the software type (execute for python/perl, compile and execute for c/c++)

class Backdoors:
    def __init__(self):
        return 
    
class Interface:
    def __init_(self):
        return 

class Session:
    def __init__(self):
        return

banner = open("ascii_banner", "rb")
s = banner.read().decode("utf-8")
print(s)