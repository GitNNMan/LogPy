from colorama import init, Fore
#import logging
import datetime
import time
init()


filename =''
def File(self,filename):
    f = open(filename,'w')
def SaveLog():
    pass


def logtime():
    """Формирует дату формата [2020-12-31  23:59:59] и возвращает её в формате string
    """
    today = datetime.datetime.today()
    return today.strftime("[%Y-%m-%d  %H:%M:%S]")

class LogPrint:
    def __init__(sefl):
        print(Fore.CYAN+logtime()+"[INFO] Система логирования активирована"+Fore.RESET)
    def INFO(self,tetxmsg):
        print(Fore.CYAN+logtime()+"[INFO] "+tetxmsg+Fore.RESET)
    def ERRORS(sefl,textmsg):
        print(Fore.RED+logtime()+"[ERROR] "+textmsg+Fore.RESET)
    def MESSAGE(sefl, textmsg):
        print(Fore.GREEN+logtime()+"[MASSAGE] "+textmsg+Fore.RESET)
    def LOG(sefl, tetxmsg):
        print(Fore.YELLOW+logtime()+"[LOG] "+tetxmsg+Fore.RESET)
    def DEBUG(sefl,tetxmsg):
        print(Fore.MAGENTA+logtime()+"[DEBUG] "+tetxmsg+Fore.RESET)
    def OTHER(sefl,tetxmsg):
        print(Fore.BLUE+logtime()+"[OTHER] "+tetxmsg+Fore.RESET)
        
class LogSave:
    def __init__(self):
            pass

c = LogPrint()

c.INFO("INFO")
c.ERRORS("ERRORS")
c.LOG("LOG")
c.MESSAGE("MESSAGE")
c.DEBUG("DEBUG")
time.sleep(10)
c.OTHER("OTHER")


# TODO Начальные установки (файл и т.д.)
# ! Добавить DEBUG, Warrning, critical
