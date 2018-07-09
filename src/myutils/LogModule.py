import logging
import os
import sys
import datetime

loggerA = logging.getLogger("analyze")
loggerD = logging.getLogger("detail")

def setInfoLogging(filename=''):

    if not filename:
        day = datetime.datetime.now()
        time_index = '{0}-{1}-{2}'.format(day.year, day.month, day.day)
        # time_index = "%s-%s-%s" %(day.year, day.month, day.day)
        processdir = sys.path[0]
        path = os.path.join(processdir, "AnalyzeLog")
        if os.path.exists(path) == False:
            os.mkdir(path)
        else:
            pass

        filename = path + '\\analyze_%s.log' %time_index

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename= filename,
                        filemode='a')

    #################################################################################################
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(lineno)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('analyze').addHandler(console)
    #################################################################################################

def setDetailLogging(filename=''):

    if not filename:
        day = datetime.datetime.now()
        time_index = '{0}-{1}-{2}'.format(day.year, day.month, day.day)
        processdir = sys.path[0]
        path = os.path.join(processdir, "DetailLog")
        if os.path.exists(path) == False:
            os.mkdir(path)
        else:
            pass

        filename = path + '\\detail_%s.log' %time_index

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=filename,
                        filemode='a')

    #################################################################################################
    #定义一个StreamHandler，将ERROR级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(lineno)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('detail').addHandler(console)
    #################################################################################################
