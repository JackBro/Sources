#!/usr/bin/env python
# -*- coding: gbk -*-
__author__ = 'QiYunhu-13111020'
'''
    ��ʵ�ֻ���һ���ַ�һ���ַ������

                                2014-11-26
'''

from time import sleep
import sys
#�ڶ���������ÿ���ַ������ʱ��ļ��ʱ��
def slowPrint( s , time = 0.0009 ) :
    for ch in s :
        sys.stdout.write( ch )
        sys.stdout.flush( )
        sleep( time )
#������
if __name__ == '__main__' :
    slowPrint( "[+] Every one is a moon and has a dark side which never shows to others." )
    slowPrint( "[+] Every one is a moon and has a dark side which never shows to others." , 0.1 )
    slowPrint( "[+] Every one is a moon and has a dark side which never shows to others." )
