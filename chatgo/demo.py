#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'demo'
__author__ = 'JieYuan'
__mtime__ = '2019-05-10'
"""

import os
from wxpy import *

# 方便扫码登录
cmd = 'mkdir ./wxftp && cd ./wxftp && python -m http.server 8080'
os.system(cmd)

bot = Bot()
bot.enable_puid()  # 启用聊天对象的puis属性
bot.self.nick_name  # 登录微信的昵称

# 设置历史消息的最大保存数量为 10000 条
bot.messages.max_history = 10000
Bot.register()
# 好友统计
bot.friends().stats_text()  # bot.friends().stats()

# @bot.register()
# def just_print(msg):
#     # 打印消息
#     print(msg)
#
# bot.registered.disable(just_print)
# bot.registered.enable(just_print)
