#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'similar'
__author__ = 'JieYuan'
__mtime__ = '2019/4/24'
"""

from gensim.models import fasttext

model = fasttext.load_facebook_model('/home/yuanjie/desktop/南京小米算法共享/WordVectors/cbow.comment')


def get(input):
    answer = model.wv.similar_by_word(input)
    answer = ':\n' + '\n'.join(map(lambda x: '%.3f %s' % (x[1], x[0]), answer))
    return answer
