#-*- coding:utf-8 -*-

from locust import HttpLocust, TaskSet, task

# host = "https://jbt.sinoecare.net"
host = "https://www.baidu.com"

class UserBehavior(TaskSet):

    # def on_start(self):
    #     ''' 获取全局生成器 用户名密码'''
    #     global OPInfo_glb
    #     OPInfoData = next(OPInfo_glb).split(',')
    #     # print ('username : ' + OPInfoData[0] + ' password: ' + OPInfoData[1])
    #
    #     values = {}
    #     values['name'] = OPInfoData[0].strip()
    #     values['userKey'] = "4DF="
    #     values["pwd"] = OPInfoData[1].strip()
    #     values["verifyCode"] = 'verifycode'
    #
    #     with self.client.request(method="POST", url="/login/toLogin", data=values, catch_response=True) as response:
    #         response.raise_for_status()
    #         rsp_dataII = response.json()
    #         print(rsp_dataII)

    @task
    def RealTimeCharge(self):

        values = {}
        values['xnbChargePhone'] = "11111111111"
        values['chargeLevelNow'] = "300"
        values['chargeAmountNow'] = "300"
        values['xnbchargeType'] = "0"

        with self.client.request(method="POST", url="/", catch_response=True, name="RealTimeCharge") as response:

            response.raise_for_status()

            try:
                rsp_data = response.text

            except Exception as e:
                print(e)
                response.failure(e)
                return

            # print(rsp_data)

        arg = {}
        arg['a'] = 'asdf'

        self.schedule_task(self.RealTimeChargeII, kwargs= arg)

    def RealTimeChargeII(self, a):
        print (a)

        values = {}
        values['xnbChargePhone'] = "11111111111"
        values['chargeLevelNow'] = "300"
        values['chargeAmountNow'] = "300"
        values['xnbchargeType'] = "0"

        with self.client.request(method="POST", url="/", catch_response=True, name="RealTimeCharge") as response:

            response.raise_for_status()

            try:
                rsp_data = response.text

            except Exception as e:
                print(e)
                response.failure(e)
                return

            # print(rsp_data)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 800
    host = host
