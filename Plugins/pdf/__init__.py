import logtool
import pluginmanger
import os
import pdfplumber


class Plugin:
    def __init__(self):
        self.log = logtool.addlog("...")
        self.log.info("Pdf plugin run")

    def init(self, pm: pluginmanger.PluginM):
        self.log.info("Init")
        pm.add_lock(self.find, "FIND")
        return True

    def find(self, path: str, find_str: str) -> bool:
        if not os.path.splitext(path)[-1] == ".pdf":
            return False
        with pdfplumber.open(path) as f:
            for page in f.pages:
                if find_str in page.extract_text():
                    return True
