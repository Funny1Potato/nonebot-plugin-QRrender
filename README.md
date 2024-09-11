<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-QRrender

_✨ 将文本转为二维码，可自定义样式 ✨_



</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>



## 📖 介绍

本插件使用[Amazing-QR](https://github.com/x-hw/amazing-qr)生成器生成二维码

可生成常见的二维码，以及有图片背景的艺术二维码

## 💿 安装


<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-QRrender



## ⚙️ 配置
请在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项  | 必填 | 默认值 |          说明           |
| :----: | :--: | :----: | :--------------------: |
| QR_res |  否  |   5    | 二维码大小（范围为1~40） |



## 🎉 使用
插件自带指令文档，发送 `QR帮助` 即可获取指令文档

### 生成二维码
发送 `QR 文本` 即可生成二维码，若bot有设置命令前缀，需加命令前缀，如 `/`

支持的参数：模板

使用方法： `QR 文本 模板名` ，模板需自行上传或命名为`模板名.jpg`后添加至`data\QRrender\library`文件夹内

示例：
```
QR 114514 homo
QR 1919810
```
上述指令将会生成
```
内容为“114514”，背景是名为“homo”的模板图片的二维码
内容为“1919810”的普通二维码
```

### 上传图片模板
发送 `QR模板` 即可根据提示上传图片并命名

支持以`回复`、`附图`等方式直接上传图片并命名。例：

<img src="https://github.com/Funny1Potato/nonebot-plugin-QRrender/blob/main/example.jpg" width="240">

## 可能遇到的问题

目前没发现（）


## 将来可能支持的功能

□支持扫码功能？

□支持gif动图

□...

## 还有些想说的
本仓库使用了nonebot-plugin-template的模板，谨向作者表示感谢

本人为普通大学生，并非计算机类的专业，水平有限，如有问题或建议请直接发issue，我会尽量解决
