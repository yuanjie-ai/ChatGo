#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
__title__ = 'tuling'
__author__ = 'JieYuan'
__mtime__ = '2019/4/24'
"""
import requests

url = 'http://www.tuling123.com/openapi/api?key=3ac26126997942458c0d93de30d52212&info='
get = lambda q: requests.get(url + q).json()['text']