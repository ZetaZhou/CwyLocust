__author__ = 'Administrator'
# -*- coding:utf-8 -*-

import cx_Oracle

from myutils.myUtils import *
from myutils.sqlSelect import *

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

    def insertBaseFieldDetail(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO BASE_FIELD_DETAIL (FIELD_DETAIL_ID, FIELD_ID, FIELD_NAME, FIELD_TYPE, INPUT_TYPE, INPUT_MUST, ADD_MAN, ADD_TIME, UPD_TIME, VERSION)" \
            " VALUES (SEQ_BASE_FIELD_DETAIL.NEXTVAL, :1, :2, 'buss', :3, '0', '10000498', sysdate, sysdate, '1')")

        cr.executemany(None, datalist)

    def insertSysUser(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO SYS_USER (USER_ID, USER_NAME, PHONE, PWD, USER_TYPE, D_INST_CODE, STATUS, ERR_TIMES, ADD_TIME, UPD_TIME, VERSION)" \
            " VALUES (SEQ_SYS_USER.NEXTVAL, :1, :2, :3, :4, :5, :6, 0, sysdate, sysdate, 1 )")

        cr.executemany(None, datalist)

    def insertBaseTemplate(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO BASE_TEMPLATE (TEMPLATE_ID, TEMPLATE_NAME, TEMPLATE_DEPT, OWNER, CLICK_NUM, FLAG, ADD_TIME, UPD_TIME, VERSION)" \
                   " VALUES (SEQ_BASE_TEMPLATE.NEXTVAL , :1, '1', '10000498', '1', '1', sysdate, sysdate, '1')")

        cr.executemany(None, datalist)

    def insertBaseTemplateDetail(self, datalist):
        db = self.db
        cr = db.cursor()

        cr.prepare("INSERT INTO BASE_TEMPLATE_DETAIL (TEMPLATE_DETAIL_ID, TEMPLATE_ID, FIELD_ID, FIELD_DETAIL_ID, FIELD_NAME, INPUT_TYPE, COLUMNS, ADD_TIME, UPD_TIME, VERSION, FIELD_ORDER)" \
                   " VALUES (SEQ_BASE_TEMPLATE_DETAIL.NEXTVAL , :1, :2, :3, :4, :5, :6, sysdate, sysdate,'1', :7)")

        cr.executemany(None, datalist)

    def close(self):
        db = self.db
        cr = db.cursor()

        cr.close()
        db.commit()
        db.close()


if __name__ == '__main__':
    insert = OrclInsert()
    select = oracleSelect()

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

    # xzqh = '4201' + '%'
    # xzqhlist = insert.getInstCode(xzqh)                  # 获取行政区划
    # # xzqhlistNew = list(filter(filterXzqh, xzqhlist))
    # # print (xzqhlistNew[0][0][-2:])
    # # print (len(xzqhlistNew))
    #
    # sysuserlist = creatSysUser(xzqhlist)
    # print (sysuserlist)
    # insert.insertSysUser(sysuserlist)

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

    '''
    获取云字段列表
    创建字段详情信息
    插入字段详情表
    '''
    # basefieldlist = select.getBaseField()
    # # print(baseFieldlist)
    # basefielddetaillist = creatBaseFieldDetailList(basefieldlist)
    # # print (basefielddetaillist)
    # insert.insertBaseFieldDetail(basefielddetaillist)

    '''
    创建模板数据列表
    插入模板表
    '''
    # basetempdatalist = creatBaseTemplateList()
    # print(basetempdatalist)
    # insert.insertBaseTemplate(basetempdatalist)

    '''
    获取云字段库数据列表
    获取并创建云字段库详情信息列表
    '''
    # basefieldlist = select.getBaseField()
    # # print (basefieldlist)
    # basefielddetaillist = select.getBaseFieldDetail(basefieldlist)
    # print (basefielddetaillist)
    basefielddetaillist = select.getBaseFieldDetailII()
    basetemplatelist = creatBaseTemplateDetailList(basefielddetaillist)
    insert.insertBaseTemplateDetail(basetemplatelist)


    insert.close()
    select.close()

