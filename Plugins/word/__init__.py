import logtool
import pluginmanger

class Plugin:
    def __init__(self):
        self.log = logtool.addlog("...")
        self.log.info("Word plugin run")

    def init(self,pm:pluginmanger.PluginM):
        self.log.info("Init")
        return True