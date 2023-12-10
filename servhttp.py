import webserv
import webbrowser
import os
import random
import ctypes
from myfunc import myfunc
from tkinter import messagebox
from platform import system

def main():
    HOST = '127.0.0.1'
    iniPORT = 50000
    newPORT = random.randint(50000,60000)
    CODESTR = "hrdirective"
    isrepliyed = 0

    try:
        arglist = []

        arglist.append('"' + 'user' + '":"' + os.getlogin() + '"')
        querystr = "{" + ",".join(arglist) + "}"

        currentfolder =  os.path.dirname(os.path.realpath(__file__))

        if system() == 'Windows':
            ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0)
        #

        htmlfilepath = "file://" + currentfolder + "/index.html"

        webbrowser.open(htmlfilepath) #open html file of the UI

        serv = webserv.HttpServer((HOST,iniPORT),webserv.Handler,CODESTR,newPORT,myfunc,querystr)

        while isrepliyed == 0:
            isrepliyed = serv.run_once()
        #

        serv.close()
        serv = webserv.HttpServer((HOST,newPORT),webserv.Handler,'',newPORT,myfunc,querystr)
        serv.run_continuously()
    #
    except Exception as e:
        messagebox.showerror("Main", e)
    #
#

if __name__ == "__main__":
    main()
#