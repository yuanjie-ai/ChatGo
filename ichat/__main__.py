#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'demo'
__author__ = 'JieYuan'
__mtime__ = '19-3-22'
"""

from pprint import pprint

import requests
import itchat
from utils import model
from utils import BaiduPost, topnews, tuling

api = BaiduPost()


@itchat.msg_register(['Text', 'Picture'], isGroupChat=True)
def text_reply(msg):
    username = msg['User']['NickName']  # 群名
    # username = msg['ActualNickName']  # 群成员的昵称
    question = msg['Text']
    print(username, question)

    if isinstance(question, str) and question.startswith('@'):
        if question.startswith('@AI坚持'):
            _, item, input = question.split()

            if '求夸' in question:
                answer = '语料未更新'
                itchat.send(answer, msg['FromUserName'])
            elif item == '相似词':
                answer = model.wv.similar_by_word(input)
                answer = '相似词 Top 10: \n' + '\n'.join(map(lambda x: '%.3f %s' % (x[1], x[0]), answer))
                itchat.send(answer, msg['FromUserName'])

            elif item == 'topnews':
                answer = '热点新闻：'+ '\n\n'.join(topnews.titles[:int(input)])
                itchat.send(answer, msg['FromUserName'])









            elif question.split()[-1] == '写诗':
                answer = api.predict({'text': question.split()[1]},
                                     'https://aip.baidubce.com/rpc/2.0/nlp/v1/poem')['poem']
                answer = answer[0]['content'].strip().replace('\t', '\n')
                itchat.send(answer, msg['FromUserName'])

            elif question.split()[-1] == '春联':
                answer = api.predict({'text': question.split()[1]},
                                     'https://aip.baidubce.com/rpc/2.0/nlp/v1/couplets')['couplets']
                answer = f"中： {answer['center']}\n上： {answer['first']}\n下： {answer['second']}"

                itchat.send(answer, msg['FromUserName'])

            else:
                answer = tuling.get(''.join(question.split()[1:]))
                itchat.send(answer, msg['FromUserName'])
        # else:
        #     itchat.send('@me求夸吧', msg['FromUserName'])


# @itchat.msg_register(['Text'], isFriendChat=True)
# def text_reply(msg):
#     username = msg['User']['NickName']
#     question = msg['Text']
#
#     if isinstance(question, str) and '饕餮' in username:
#         answer = requests.get(url + question).json()['text']
#         answer = f'@你的小可爱\n{answer}'
#         itchat.send(answer, msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
