#-*- coding:utf-8 -*-

'''
@ auther: ZetaZhou
'''

import random

from xpinyin import Pinyin
from myutils.xingming import *

p = Pinyin()

dict = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}

def creatDataList(instlist):

    datalist = []

    for inst_code in instlist:

        index = '01'

        for i in range(1, 2000 + 1):

            xing = ''.join(random.sample(Xing, 1))
            ming = ''.join(random.sample(Ming, 2))
            CUST_NAME = xing + ming

            if int(inst_code[0][6:8]) > 25 :
                index = '02'
                day = '%02d' %(int(inst_code[0][6:8]) - 15)
            else:
                day = inst_code[0][6:8]

            mouthday = index + day

            id_card = inst_code[0][0:6] + '19' + '%02d' % (70 + int(inst_code[0][-2:])) + mouthday + '%04d' %i

            datalist.append([inst_code[0], CUST_NAME, id_card])

    return datalist

def creatXzqhList():

    xzqhInit = '4201'
    xzqhnameInit = '中国-湖北省-武汉市'
    xzqhlist = []

    for n in range(1,50):

        xzqhLv = '3'
        xzqhXj = xzqhInit + "%02d" %n
        nameXj = ''.join(random.sample(Xing + Ming, 1)) + '区'
        xzqhnameXj = xzqhnameInit + '-' + nameXj
        spellFirst = p.get_initials(nameXj, '')
        spellAll = p.get_pinyin(nameXj, '')

        xzqhlist.append([xzqhXj, nameXj, xzqhnameXj, xzqhLv, spellFirst, spellAll])

        for i in range(1,30 + 1):

            xzqhLv = '4'
            xzqhZj = xzqhXj + "%02d" %i
            nameZj = ''.join(random.sample(Xing + Ming, 2)) + '镇'
            xzqhnameZj = xzqhnameXj + '-' + nameZj
            spellFirst = p.get_initials(nameZj, '')
            spellAll = p.get_pinyin(nameZj, '')
            xzqhlist.append([xzqhZj, nameZj, xzqhnameZj, xzqhLv, spellFirst, spellAll])

            for o in range(1, 15 + 1):

                xzqhLv = '5'
                xzqhCj = xzqhZj + "%03d" %o
                nameCj = ''.join(random.sample(Xing + Ming, 3)) + '村'
                xzqhnameCj = xzqhnameZj + '-' + nameCj
                spellFirst = p.get_initials(nameCj, '')
                spellAll = p.get_pinyin(nameCj, '')
                xzqhlist.append([xzqhCj, nameCj, xzqhnameCj, xzqhLv, spellFirst, spellAll])

    return xzqhlist

def creatBaseFieldList():

    basefieldlist = []
    for i in range(50000):
        fieldname = "云字段%05d" %i
        basefieldlist.append([fieldname, 'buss'])

    return basefieldlist

def creatSysInstModuleList(xzqhlist):

    newlist = []
    for xzqh in xzqhlist:

        newlistII = []
        for i in range(2, 22):
            newlistII.append([xzqh[0], str(i)])

        newlist.append(newlistII)

    return newlist

def creatSysUser(xzqhlist):

    YHlist = []
    Phone = 10000000000
    index = 1
    for xzqh in xzqhlist:
        Phone += 1
        Username = ''.join(list(map(lambda x: dict[x], str(index))))
        Pwd = 'b2c0b6bb9c15c993ad41451a87b1f709b374e6a910d8f23a20b1d96f'
        UserType = 1
        XzqhCode = xzqh[0]
        Status = 1
        version = 1
        index += 1

        YHlist.append([Username, Phone, Pwd, UserType, XzqhCode, Status])

    return YHlist

def creatBaseFieldDetailList(basefieldlist):
    basefielddetaillist = []

    for basefield in basefieldlist:

        for i in range(1, 7):
            if i  == 6:
                basefielddetaillist.append([basefield[0], basefield[1], str(8)])
            else:
                basefielddetaillist.append([basefield[0], basefield[1], str(i)])

    return basefielddetaillist

def creatBaseTemplateList():
    basetempdatalist = []
    for i in range(20000):
        tempname = ''.join(list(map(lambda x: dict[x], str(i))))
        basetempdatalist.append([tempname])

    return basetempdatalist

def creatBaseTemplateDetailList(datalist):
    basetemplatelist = []

    tempindex = 1
    for i in range(20000):

        for n in range(1, 12 + 1):

            data = datalist.pop(0)
            basetemplatelist.append([str(tempindex), data[0], data[1], data[2], data[3], 'v' + str(n), str(n)])
        tempindex += 1
    return basetemplatelist


def filterXzqh(data):
    if len(data[0]) == 11:
        return data
    else:
        pass

if __name__ == '__main__':
    pass

    # xzqhlist = creatXzqhList()
    # # print (xzqhlist)
    #
    # datalist = creatDataList(xzqhlist)
    # print (datalist)

