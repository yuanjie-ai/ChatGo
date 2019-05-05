#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'meeting'
__author__ = 'JieYuan'
__mtime__ = '2019/5/5'
"""

import requests
import pandas as pd


def get(mode='merge'):
    if mode == 'merge':
        url = 'http://211.159.150.211:5000/meeting_result'
        dt = pd.datetime.now().date()
        _ = requests.get(url).json()
        _ = '\n'.join(_.get(str(dt)).values())
        return '%s 南京站会纪要：\n%s' % (dt, _)
    elif mode == 'input':
        url = 'http://211.159.150.211:5000/meeting'
        return '会议纪要填写：\n %s' % url


if __name__ == '__main__':
    print((get()))
