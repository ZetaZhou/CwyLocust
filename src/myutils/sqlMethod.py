__author__ = 'Administrator'
# -*- coding:utf-8 -*-

import cx_Oracle

from myutils.myUtils import *


class OrclInsert:

    def __init__(self):
        self.db = cx_Oracle.connect('cwy_pertest/zwht456@ORCL')

    def insertDataCust(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO DATA_CUST (CUST_ID, INST_CODE, CUST_NAME, ID_CARD, SEX, NATION, ADD_TIME)" \
                   " VALUES (SEQ_DATA_CUST.NEXTVAL , :1, :2, :3 , '男', '汉族', sysdate )")

        cr.executemany(None, datalist)

    def insertSysInst(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO SYS_INST (INST_ID, INST_CODE, INST_NAME, INST_F_NAME, INST_LV, CN_NAME, CN_F_NAME, STATUS, IS_NEW, ADD_TIME, UPD_TIME, VERSION, IS_OPEN)" \
                   " VALUES (SEQ_SYS_INST.NEXTVAL ,:1, :2, :3, :4, :5, :6, '1', '1', sysdate, sysdate, 1, 1 )")

        cr.executemany(None, datalist)

    def insertBaseField(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO BASE_FIELD (FIELD_ID, FIELD_NAME, FIELD_TYPE, ADD_TIME, UPD_TIME, VERSION, USER_ID)" \
            " VALUES (SEQ_BASE_FIELD.NEXTVAL , :1, :2, sysdate, sysdate, '1', '10000498')")

        cr.executemany(None, datalist)

    def insertSysUser(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO SYS_USER (USER_ID, USER_NAME, PHONE, PWD, USER_TYPE, D_INST_CODE, STATUS, ERR_TIMES, ADD_TIME, UPD_TIME, VERSION)" \
            " VALUES (SEQ_SYS_USER.NEXTVAL, :1, :2, :3, :4, :5, :6, 0, sysdate, sysdate, 1 )")

        cr.executemany(None, datalist)

    def getInstCode(self, xzqh):

        db = self.db
        cr = db.cursor()
        sql = "select INST_CODE from SYS_INST where inst_code like '%s' order by inst_code" %xzqh
        cr.execute(sql)
        data = cr.fetchall()
        # print (len(data))
        # for i in data:
        #     print (i)
        return  data

    def getBaseField(self):

        db = self.db
        cr = db.cursor()
        sql = "select * from BASE_FIELD_DETAIL where field_type = 'base' order by to_number(field_detail_id) desc"
        cr.execute(sql)
        data = cr.fetchall()
        # for i in data:
        #     print (i)

        return data

    def getDataCust(self):

        db = self.db
        cr = db.cursor()
        sql = "select * from DATA_CUST t where t.inst_code = '14010501'"
        cr.execute(sql)
        data = cr.fetchall()
        # for i in data:
        #     print (i)

        return data

    def setBaseTempDetal(self, dataList):

        db  = self.db
        cr = db.cursor()
        index = 1
        # print (dataList)
        for i in dataList:
            colums = 'v' + str(index)
            sql = "INSERT INTO BASE_TEMPLATE_DETAIL VALUES (SEQ_BASE_TEMPLATE_DETAIL.NEXTVAL, 1, '%s','%s', '%s', 1, '%s', '%s', sysdate, sysdate, 1, '%s')"  %(i[1], i[0], i[2], i[4], colums, index)
            print(sql)
            cr.execute(sql)
            index += 1
            db.commit()

    def setDataTask(self, dataList):

        db = self.db
        cr = db.cursor()

        index = 1
        sData = ''
        lData = ''

        for i in range(1, 100):
            if i < 51:
                sData = ",'" + str(i)+ "'" + sData
            else:
                lData = ",'' " + lData

        lastData = sData + lData
        # print (lastData)

        for i in dataList:
            sql = "INSERT INTO DATA_TASK " \
                  "VALUES (SEQ_DATA_TASK.NEXTVAL, 1, 1, '%s',  '14010501', '%s', '%s' %s, Null, 1, '10000445', '10000445', sysdate, sysdate, 1)" %(i[0], i[3], i[2],lastData)
            print(sql)
            cr.execute(sql)
            index += 1
            db.commit()

    def getBaseTempDetail(self):
        datalist = []
        db = self.db
        cr = db.cursor()

        sql = 'select columns, base_columns from BASE_TEMPLATE_DETAIL'
        cr.execute(sql)
        data = cr.fetchall()

        for i in data:
            if 'Time' in i[1]:
                datalist.append(i)

        print (datalist)

    def close(self):
        db = self.db
        cr = db.cursor()

        cr.close()
        db.commit()
        db.close()


if __name__ == '__main__':
    insert = OrclInsert()

    '''
    添加人表数据
    '''
    # for i in range(1, 2):
    #     xzqh = '4201' + '%02d' %i + '%'
    #     xzqhlist = insert.getInstCode(xzqh)                  # 获取行政区划
    #     xzqhlistNew = list(filter(filterXzqh, xzqhlist))
    #     # print (xzqhlistNew[0][0][-2:])
    #     # print (len(xzqhlistNew))
    #
    #     peoplelist = creatDataList(xzqhlistNew)
    #     print (peoplelist)
    #     print ("PeopleList created success for loop %d" %i)
    #
    #     insert.insertDataCust(peoplelist)
    #     print ("insert datacust success for loop %d" %i)

    '''
    添加操作用户数据
    '''

    xzqh = '4201' + '%'
    xzqhlist = insert.getInstCode(xzqh)                  # 获取行政区划
    # xzqhlistNew = list(filter(filterXzqh, xzqhlist))
    # print (xzqhlistNew[0][0][-2:])
    # print (len(xzqhlistNew))

    sysuserlist = creatSysUser(xzqhlist)
    print (sysuserlist)
    insert.insertSysUser(sysuserlist)

    '''        
    添加行政区划
    '''
    # xzqhlist = creatXzqhList()
    # insert.insertSysInst(xzqhlist)

    '''
    获取字段表信息
    插入模版详情表
    '''
    # datalist = insert.getBaseField()
    # insert.setBaseTempDetal(datalist)

    '''
    获取人表详情
    插入任务表
    '''
    # datalist = insert.getDataCust()
    # insert.setDataTask(datalist)

    '''
    获取模版详情表
    '''
    # insert.getBaseTempDetail()

    '''
    插入字段数据
    '''
    # basefieldlist = creatBaseFieldList()
    # print(basefieldlist)
    # insert.insertBaseField(basefieldlist)

    insert.close()

