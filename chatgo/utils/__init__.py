#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '__init__.py'
__author__ = 'JieYuan'
__mtime__ = '19-3-22'
"""
from .baidu import BaiduPost


# 注册好友请求类消息
@bot.register()  # 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    global a
    a = msg

    if '功能' in msg.text.lower():  # 判断好友请求中的验证文本
        new_friend = bot.accept_friend(msg.card)  # msg.card 为该请求的用户对象
        # 或 new_friend = msg.card.accept()
        new_friend.send('[坏笑]哈哈，我自动接受了你的好友请求')

def update_group(keys=['闲聊']):
    groups = []
    for key in keys:
        groups += bot.groups(True).search(key)
    for group in groups:
        group.update_group(True)
    return groups

gs = update_group(['闲聊', '吃饭'])

@bot.register(gs, except_self=True)# 自动接受验证信息中包含 'wxpy' 的好友请求
def groups_synchronize(msg):
    print(msg)
    prefix = '来自 %s 的 %s\n%s\n' % (msg.sender.name, msg.member.name, '-'*32)
    sync_message_in_groups(msg, gs[:1], prefix)