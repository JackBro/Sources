#-*- coding=utf-8 -*-

#���ļ����е� ����ʮ���� �滻������
#ֻ�������֣����� ��ʮ����֮���Ҫ�����±�

import os
import sys
index = { 
    "һ" : "1" ,
    "��" : "2" ,
    "��" : "3" ,
    "��" : "4" ,
    "��" : "5" ,
    "��" : "6" ,
    "��" : "7" ,
    "��" : "8" ,
    "��" : "9" , }
for dirname, dirnames, filenames in os.walk('.') :
    for filename in filenames :
        if ".py" not in filename :
            os.rename( filename , filename[:2] + index[filename[2:4]] + index[filename[6:8]] + filename[8:] )
#            print filename[2:8] + " -> " + index[filename[2:4]] + index[filename[6:8]]
#            print filename[:2] + index[filename[2:4]] + index[filename[6:8]] + filename[8:]