import logtool
import loguru
import importlib
import os


class PluginM:

    def __init__(self,initplugins: dict):
        self.plog = logtool.addlog("PluginManger")
        self.plog.info("")
        self.plugins = {}
        self.events = {"READ":[],"FIND":[]}
        self.load_plugins(initplugins)

    def __load_plugin(self, name: str, id: str) -> bool:
        self.plog.info("加载插件 {} id：{}".format(name, id))
        if not os.path.isdir("./Plugins/{}".format(id)):
            self.plog.warning("未找到此插件")
            return False
        else:
            self.plog.info("已找到此插件，准备加载")
            try:
                p = importlib.import_module(name="Plugins.{}".format(id))
            except ModuleNotFoundError as e:
                self.plog.warning("加载失败，错误：{}".format(str(e)))
                return False
            p = p.Plugin()
            self.plog.info("加载成功")
            if p.init(self):
                self.plog.success("插件初始化成功")
                self.plugins.update({name: p})
                return True
            else:
                self.plog.warning("插件初始化失败，请检查日志文件")
                return False

    def load_plugins(self, plugins: dict):
        """
        Load plugins
        :param plugins: 一个字典，格式为名称:位置
        :return:
        """
        datas = {"success": 0, "all": 0, "error": 0}
        for index, path in plugins.items():
            self.plog.info("加载 {}".format(index))
            datas["all"] += 1
            if self.__load_plugin(index, path):
                self.plog.success("Plugin {} 加载成功".format(index))
                datas["success"] += 1
            else:
                self.plog.warning("Plugin {} 加载失败".format(index))
                datas["error"] += 1
        self.plog.success("插件加载完成")
        self.plog.info("共加载插件 {} 个，成功 {} 个，失败 {} 个".format(datas["all"], datas["success"], datas["error"]))

    def add_lock(self, lock, event_id: str | int) -> bool:
        if event_id in self.events.keys():
            self.events[event_id].append(lock)
            return True
        else:
            return False

    def do_event(self, event_id, *args, **kwargs) -> list:
        result = []
        for i in self.events[event_id]:
            result.append(i(*args,**kwargs))
        return result

    def add_event(self, event_id):
        self.plog.info(...)
        self.events.update({event_id, []})
        self.plog.success(...)
