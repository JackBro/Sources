#-*- coding=utf-8 -*-

#����ȥ����gerrit�����Ĵ����ߴ��г����������׺
#ȥ�������һ����ܣ���������չ���ĵ�֮����ַ�

import os
import sys
for dirname, dirnames, filenames in os.walk('.') :
    for filename in filenames :
        if ".py" not in filename :
            # print filename[:filename.rfind('-')] + filename[filename.rfind('.'):]
            os.rename( filename , filename[:filename.rfind('-')] + filename[filename.rfind('.'):] )