import logtool
import pluginmanger
import os


class Plugin:
    def __init__(self):
        self.log = logtool.addlog("...")
        self.log.info("text plugin run")

    def init(self, pm: pluginmanger.PluginM):
        self.log.info("Init")
        pm.add_lock(self.find, "FIND")
        return True

    def find(self, path: str, find_str: str) -> bool:
        if not os.path.splitext(path)[-1] == ".txt":
            return False
        with open(path) as f:
            if find_str in f.read():
                return True
            else:
                return False
