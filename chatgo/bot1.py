#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'bot1'
__author__ = 'JieYuan'
__mtime__ = '2019-05-13'
"""
import os
from wxpy import *

os.popen('python -m http.server 7777')

bot = Bot()


# 好友验证：注册好友请求类消息
@bot.register(msg_types=FRIENDS)  # 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # if '功能' in msg.text.lower():  # 判断好友请求中的验证文本
    new_friend = bot.accept_friend(msg.card)
    new_friend.send('[坏笑]您好，我是微信助手！')


# 群信息同步
def update_group(keys=['闲聊']):
    groups = []
    for key in keys:
        groups += bot.groups(True).search(key)
    for group in groups:
        group.update_group(True)
    return groups


gs = update_group(['闲聊', '吃饭'])


@bot.register(gs, except_self=True)  # 自动接受验证信息中包含 'wxpy' 的好友请求
def groups_synchronize(msg):
    prefix = '来自 %s 的 %s\n%s\n' % (msg.sender.name, msg.member.name, '-' * 32)
    # sync_message_in_groups(msg, gs[:1], prefix) # 单向转发
    sync_message_in_groups(msg, gs[:1], prefix)
