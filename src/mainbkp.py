#-*- coding:utf-8 -*-

'''
@ auther: ZetaZhou
'''

#-*- coding:utf-8 -*-

from locust import HttpLocust, TaskSet

from src.myutils.commom import *

host = "http://192.168.1.245:8081"

OPInfo_glb = GetOpInfo()

def villLogin(obj):

    values = {}
    values['username'] = next(getOpInfo)
    values['password'] = next(PeopleIdV2_glb)


    with obj.client.request(method="POST", url="/test/charge", data=values, catch_response=True, name = "RealTimeCharge") as response:
        response.raise_for_status()
        try:
            rsp_data = response.json()
        except Exception as e:
            response.failure(e)
            return

        if rsp_data['code'] == "0000":
            response.success()
        else:
            if "个人缴费当年预核定失败" in rsp_data['msg']:
                response.success()
            elif "查无此人" in rsp_data['msg']:
                response.success()
            else:
                response.failure('dongruan Method failed')
        # print ("PeopleId: ", values["peopleId"])
        # print (rsp_data['msg'])

class UserBehavior(TaskSet):
    # tasks = {RealTimeCharge: 2, GetDongruanPeopleInfoYcx: 2, GetDongruanPeopleInfoDn: 2, GetDongruanPeopleInfoBj: 2}
    tasks = {villLogin: 1}
    # tasks = {GetDongruanPeopleInfoYcx: 1, GetDongruanPeopleInfoDn: 1, GetDongruanPeopleInfoBj: 1}

    # def on_start(self):
    #     '''
    #     :return:
    #     :登录获取session
    #     '''
    #
    #     ''' 获取全局生成器 用户名密码'''
    #     global OPInfo_glb
    #     OPInfoData = next(OPInfo_glb).split(',')
    #     print ('username : ' + OPInfoData[0] + ' password: ' + OPInfoData[1])
    #
    #     values = {}
    #     values['username'] = OPInfoData[0].strip()
    #     values["password"] = OPInfoData[1].strip()
    #
    #     with self.client.request(method="POST", url="/vill/login", data=values, catch_response=True) as response:
    #         response.raise_for_status()
    #         rsp_dataII = response.json()
    #         print(rsp_dataII)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 800
    host = host
