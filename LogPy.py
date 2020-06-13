from colorama import init, Fore
#import logging
import datetime
import time
init()

filename= ''
def FileWR(filename,msgtext):
    f = open(filename,'a+')
    f.write(msgtext)
    f.close()
    
class FileWriteLog:
    def __init__ (sefl):
        pass

    def WriteLog(sefl, WriteStr):
            pass #! Записать функцию записи строки в файл

def logtime():
    """Формирует дату формата [2020-12-31  23:59:59] и возвращает её в формате string
    """
    today = datetime.datetime.today()
    return today.strftime("[%Y-%m-%d  %H:%M:%S]")

class LogPrint:
    def __init__(self):
        print(Fore.CYAN+logtime()+"[INFO] Система логирования активирована"+Fore.RESET)
    def INFO(self, tetxmsg):
        commsg = logtime()+"[INFO] "+tetxmsg
        print(Fore.CYAN+commsg+Fore.RESET)
    def ERRORS(self, textmsg):
        commsg = logtime()+"[ERROR] "+textmsg
        print(Fore.RED+commsg+Fore.RESET)
    def MESSAGE(self, textmsg):
        commsg = logtime()+"[MASSAGE] "+textmsg
        print(Fore.GREEN+commsg+Fore.RESET)
    def LOG(self, tetxmsg):
        commsg = logtime()+"[LOG] "+tetxmsg
        print(Fore.YELLOW+commsg+Fore.RESET)
    def DEBUG(self, tetxmsg):
        commsg = logtime()+"[DEBUG] "+tetxmsg
        print(Fore.MAGENTA+commsg+Fore.RESET)
    def OTHER(self, tetxmsg):
        commsg = logtime()+"[OTHER] "+tetxmsg
        print(Fore.BLUE+commsg+Fore.RESET)
        
class LogSave:
    def __init__(self):
        pass
    def INFOsave(self,msgtext):
        commsg = logtime()+"[INFO] "+msgtext
        print(Fore.CYAN+commsg+Fore.RESET)
        commsg = commsg+"\n"
        FileWR(filename,commsg)
        


# TODO Начальные установки (файл и т.д.)
