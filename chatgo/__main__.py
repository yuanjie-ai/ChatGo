#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'demo'
__author__ = 'JieYuan'
__mtime__ = '19-3-22'
"""

import itchat
from .utils import topnews, tuling, sim, meeting


@itchat.msg_register(['Text', 'Picture'], isGroupChat=True)
def text_reply(msg):
    _send = lambda answer: itchat.send(answer, msg['FromUserName'])

    username = msg['User']['NickName']  # 群名
    # username = msg['ActualNickName']  # 群成员的昵称
    question = msg['Text']
    print(username, question)

    if isinstance(question, str) and question.startswith('@AI坚持'):
        if len(question.split()) > 2:  # 多参数：项目名+入参
            args = question.split()[1:]

            if args[0] == '相似词':
                answer = sim.get(args[1])
                _send(args[0] + answer)

            elif args[0] == 'topnews':
                answer = topnews.get(int(args[1]))
                _send(args[0] + answer)

            elif args[0] == '站会':
                answer = meeting.get()
                _send(args[0] + answer)



        else:  # 一参数：入参
            answer = tuling.get(question[6:])
            _send(answer)

            # elif question.split()[-1] == '写诗':
            #     answer = baidu.api.predict({'text': question.split()[1]},
            #                                'https://aip.baidubce.com/rpc/2.0/nlp/v1/poem')['poem']
            #     answer = answer[0]['content'].strip().replace('\t', '\n')
            #     itchat.send(answer, msg['FromUserName'])
            #
            # elif question.split()[-1] == '春联':
            #     answer = baidu.api.predict({'text': question.split()[1]},
            #                                'https://aip.baidubce.com/rpc/2.0/nlp/v1/couplets')['couplets']
            #     answer = f"中： {answer['center']}\n上： {answer['first']}\n下： {answer['second']}"
            #
            #     itchat.send(answer, msg['FromUserName'])


def run():
    itchat.auto_login()
    itchat.run()


if __name__ == '__main__':
    run()
