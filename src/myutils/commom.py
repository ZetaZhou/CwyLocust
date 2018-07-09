#-*- coding:utf-8 -*-

'''
@ auther: ZetaZhou
'''


def GetOpInfo():
    with open('.\myutils\ceshi400ren.txt', 'r') as name_txt:
        for userInfo in name_txt.readlines():
            yield userInfo


# def GetLoginVerifycode(obj):
#     ''' 获取验证码图片byte流 '''
#     with obj.client.request(method="GET", url="/getcaptcha.sl") as response:
#         rsp_data = response.content
#         verifycode = CheckSumModule.CheckSum(rsp_data)
#     return verifycode