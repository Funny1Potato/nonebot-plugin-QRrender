from nonebot import get_driver,get_plugin_config,get_bot
from nonebot.plugin import PluginMetadata
from nonebot import on_command, on_message
from nonebot.params import CommandArg,ArgPlainText,Arg,EventPlainText
from nonebot.adapters import Message
from nonebot import logger
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import (
    ActionFailed,
    Bot,
    Event,
    GroupMessageEvent,
    Message,
    MessageEvent,
    MessageSegment,
    PrivateMessageEvent,
)
from nonebot.adapters.onebot.v11.helpers import extract_image_urls
from httpx import AsyncClient
import os
from amzqr import amzqr
from pathlib import Path
from nonebot.typing import T_State
from nonebot.internal.matcher import Matcher
from .config import Config


__plugin_meta__ = PluginMetadata(
    name="二维码生成器",
    description="将文本转为二维码，可自定义样式",
    usage="发送  即可生成",
    config=Config,
    type="application",
    homepage="https://github.com/Noctulus/nonebot-plugin-QRrender",
    supported_adapters={"~onebot.v11"},
)

config = get_plugin_config(Config)

#创建目录
try:
    os.mkdir("./data")
except:
    pass
try:
    os.mkdir("./data/QRrender")
except:
    pass
try:
    os.mkdir("./data/QRrender/library")
except:
    pass


#插件指令文档
botdoc = on_command("QR帮助")

@botdoc.handle()
async def QRhelp():
    if not os.path.exists("./data/QRrender/library/help.png"):
        async with AsyncClient() as session:
            response = await session.get("https://link.funnypotato.cn/QR.png")
            open("./data/QRrender/library/help.png", "wb").write(response.content)  #下载文件
    url = Path("./data/QRrender/library/help.png")
    await botdoc.finish(MessageSegment.image(url))


#二维码生成
m = on_command("QR")
@m.handle()
async def QR(args: Message = CommandArg()):
    if data := args.extract_plain_text():           #获取文本
        try:
            words,p = data.split()
            pic = f"./data/QRrender/library/{p}.jpg"
        except:
            words = data
            pic = None
        if words == "":
            await m.finish("获取文本失败，请检查输入是否正确")
        res = config.QR_res
        amzqr.run(
            words,
            version=res,
            level='H',
            picture=pic,
            colorized=False,
            contrast=1.0,
            brightness=1.0,
            save_name="temp.png",
            save_dir="./data/QRrender"
        )                                           #生成二维码

        url = Path("./data/QRrender/temp.png")      #定位图片位置
        await m.finish(MessageSegment.image(url))
    else:
        await m.finish("获取文本失败，请检查输入是否正确")

#图片库部分
lib = on_command("QR模板")
@lib.handle()
async def s(bot: Bot, event: MessageEvent, matcher: Matcher, state: T_State, args: Message = CommandArg()):
    if name := args.extract_plain_text():
        matcher.set_arg("name", Message(name))
    message = event.reply.message if event.reply else event.message
    if imgs := message["image"]:
        matcher.set_arg("imgs", imgs)

@lib.got("imgs", prompt="请发送图片")
async def get_image(state: T_State, imgs: Message = Arg()):
    img_urls = extract_image_urls(imgs)
    if not img_urls:
        await lib.reject("获取图片失败, 请尝试重新发送")
    state["img_urls"] = img_urls

@lib.got("name", prompt="请为图片命名")
async def get_name(matcher: Matcher, state: T_State, name: str = ArgPlainText()):
    state["name"] = name
    location = Path(f"./data/QRrender/library/{name}.jpg")
    if not os.path.exists(location):
        matcher.set_arg("judge", Message("1"))
    else:
        await lib.send(MessageSegment.image(location))
        await lib.skip()

@lib.got("judge", prompt="已存在同名模板如图，扣“1”确认替换")
async def get_judge(state: T_State, judge: str = ArgPlainText()):
    if "1" in judge:
        j = "1"
    else:
        j = "0"
    state["judge"] = j

@lib.handle()
async def main(bot: Bot, event: Event, state: T_State):
    urls = state["img_urls"]
    url = urls[0]
    name = state["name"]
    direction = f"./data/QRrender/library/{name}.jpg"
    j = state["judge"]
    if j == "1":
        async with AsyncClient() as client:
            try:
                res = await client.get(url)
                open(direction, "wb").write(res.content)  #下载文件
                if res.is_error:
                    await acg_trace.finish("获取图片失败")
                else:
                    await lib.finish("保存成功")
            except:
                pass
    else:
        await lib.finish("已取消")




    


