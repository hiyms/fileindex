import sys

import logtool
import pluginmanger
import os
import yaml
import rich
from rich import markdown
from rich.table import Table

readme = markdown.Markdown("""
# Fileindex
一个用于快速检索文件的项目，由`放线菌`与`yms`提供
## 安装依赖
那可以使用如下指令来安装所有依赖：
```shell
pip3 install PyYaml rich loguru
``` 

""")

rich.print(readme)
mlog = logtool.addlog("Main")

mlog.info("Start")
config = {
    "v": 1,
    "plugins": {
    }
}


def InitPluginConfig():
    global config
    mlog.info("启动插件初始化配置程序")
    mlog.info(config)
    mlog.info("检索插件文件夹")
    if not os.path.isdir("./Plugins"):
        mlog.warning("未找到插件文件夹，准备创建")
        os.mkdir("./Plugins")
    for i in os.listdir("./Plugins"):
        mlog.info(i)
        if os.path.isdir("./Plugins/{}".format(i)):
            if os.path.isfile("./Plugins/{}/__init__.py".format(i)) and os.path.isfile(
                    "./Plugins/{}/plugin.yaml".format(i)):
                mlog.info("Find plugin {}".format(i))
                ip = logtool.mconsole.input("是否要启用此插件？ [Y/n]")
                while ip:
                    if ip == "y" or ip == "Y":
                        ip = False
                        break
                    elif ip == "N" or ip == "n":
                        ip = True
                        break
                    else:
                        mlog.warning("无法处理的输入： {}".format(ip))
                        ip = logtool.mconsole.input("是否要启用此插件？ [Y/n]")
                if not ip:
                    config["plugins"].update({i: i})


# if not os.path.isfile("./config.yaml"):
if True:
    mlog.warning("Can not find config file")
    InitPluginConfig()
    mlog.info("Creat config file")
    with open("./config.yaml", "w") as f:
        yaml.safe_dump(config, f)
        mlog.info("已写入默认配置")

mlog.info("准备加载配置")
with open("./config.yaml") as f:
    config = yaml.safe_load(f)
mlog.info("加载成功")

rich.print("配置信息：", config)

if not os.path.isdir("./.temp"):
    os.makedirs("./.temp")

pluginm = pluginmanger.PluginM(config["plugins"])
print("")

while True:
    i = logtool.mconsole.input("""
[bold]1[/bold]  插件管理
[bold]2[/bold]  搜索
[bold]3[/bold]  即将推出
[bold]4[/bold]  即将推出
[bold]q[/bold]  退出
""")
    match i:
        case "1":
            ...
        case "2":
            path = logtool.mconsole.input("请输入要搜索的根目录：")
            ruturnflag = False
            while not os.path.isdir(path):
                path = logtool.mconsole.input("[red]未找到此文件夹[/red]，请重新输入（输入'q'返回上一层）：")
                if path == "q":
                    ruturnflag = True
                    break
            if ruturnflag:
                break
            find_str = logtool.mconsole.input("请输入要查找的字符串：")
            find_paths = []
            for dirpath, __, filenames in os.walk(path):
                for filename in filenames:
                    pall = os.path.join(dirpath,filename)
                    results = pluginm.do_event("FIND",pall,find_str)
                    result = False
                    for i in results:
                        if result:
                            break
                        result = result or i
                    if result:
                        find_paths.append(pall)
            logtool.mconsole.print("共找见{}处".format(len(find_paths)))
            r_t = Table(show_header=True, header_style="bold magenta")
            r_t.add_column("",width=5)
            r_t.add_column("文件位置", style="dim")
            ind = 0
            for i in find_paths:
                ind += 1
                r_t.add_row(str(ind),i)
            logtool.mconsole.print(r_t)

        case "q":
            sys.exit()
