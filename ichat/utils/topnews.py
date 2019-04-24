#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'topnews'
__author__ = 'JieYuan'
__mtime__ = '2019/4/24'
"""

import pandas as pd

df = pd.read_html('http://web.algo.browser.miui.srv/data/feed/recall?q=topnews', encoding='utf-8')
titles = df[0][1].values.tolist()
