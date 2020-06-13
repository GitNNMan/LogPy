import LogPy
import time

LogPy.filename = "test.txt"
log = LogPy.LogPrint()
log.INFO("еррор")
time.sleep(5)
log.LOG("Попробуем")
log.filename = "e:\Logi.txt"
logsave = LogPy.LogSave()
#LogPy.File('log.txt')
logsave.INFOsave("Попытка")
logsave.INFOsave("Gjgsnrf yjvth 6")
time.sleep(5)
logsave.INFOsave("Еще попытка")