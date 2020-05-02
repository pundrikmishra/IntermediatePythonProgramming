import sys
import logging

def errpr_handling():
    return '{}. {}, line:{}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno)

try:
    a+b
except Exception as e:
    # print(str(e))
    # print(sys.exc_info())


    # print(sys.exc_info()[0])
    # print(sys.exc_info()[1])
    # print(sys.exc_info()[2])
    # print(sys.exc_info()[2].tb_frame)
    # print(sys.exc_info()[2].tb_lasti)
    # print(sys.exc_info()[2].tb_lineno)

    # print('Error: {}. {}, line:{}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))

    logging.error(errpr_handling())