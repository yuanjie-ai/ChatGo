#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
__title__ = 'meeting'
__author__ = 'JieYuan'
__mtime__ = '2019/5/5'
"""

import requests
import pandas as pd

def get(url='http://211.159.150.211:5000/meeting_result'):
    dt = pd.datetime.now().date()
    _ = requests.get(url).json()
    _ = '\n'.join(_.get(str(dt)).values())
    return '%s 南京站会：\n%s' %(dt, _)


if __name__ == '__main__':
    print((get()))