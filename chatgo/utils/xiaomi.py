#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'tables'
__author__ = 'JieYuan'
__mtime__ = '2019-04-24'
"""
import requests


def get_info(url='https://raw.githubusercontent.com/Jie-Yuan/Jie-Yuan.github.io/master/xiaomi/tables.txt'):
    _ = requests.get(url).text.strip().split()
    return ':\n' + '\n'.join(_)
