#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'topnews'
__author__ = 'JieYuan'
__mtime__ = '2019/4/24'
"""

import pandas as pd


def get(idx, url='http://web.algo.browser.miui.srv/data/feed/recall?q=topnews'):
    _ = pd.read_html(url, encoding='utf-8')[0][1].tolist()[:idx]
    return ':\n' + '\n\n'.join(_)
