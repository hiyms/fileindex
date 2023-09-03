import loguru
from sys import stdin
from rich import color, console, logging


class LogBin:
    def __init__(self):
        self.__log = console.Console()

    def success(self, text: str):
        self.__log.log(text, style="green")

    def info(self, text: str):
        self.__log.log(text)

    def warning(self, text: str):
        self.__log.log(text, style="yellow")


glog = LogBin()
mconsole = console.Console()

def addlog(logname: str):
    # l = loguru.__loguru_logger.Logger l.add(sink=stdin,format=logname + " | <green>{time:YYYY-MM-DD
    # HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{
    # line}</cyan> - <level>{message}</level>")
    return LogBin()
