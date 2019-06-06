#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'groups'
__author__ = 'JieYuan'
__mtime__ = '2019-05-13'
"""
from wxpy import *


if __name__ == '__main__':
    bot = Bot()
    bot.enable_puid()

    groups = []  # 源
    groups_ = bot.groups(True)
    for key in ['逗逼', '测试']:
        groups += groups_.search(key)

    print('*'*100)
    print(groups)

    @bot.register(groups)
    def groups_synchronize(msg):
        print(msg)
        prefix = '来自 %s 的 %s\n%s\n' % (msg.sender.name, msg.member.name, '-' * 32)
        sync_message_in_groups(msg, groups, prefix)

    bot.join()
