#!/usr/bin/env pythoy
# -*- coding: gbk -*-
__author__ = 'QiYunhu-13111020'
'''
    ����windows��linux�±��������빦��
                         2014-12-14
'''
import platform , getpass
#���жϲ���ϵͳ��Ȼ�󷵻ظ�������ϵͳ���õ�getpass����
def getpass( ) :
    Os = platform.system( )
    if( Os == 'Linux' ) :
        import sys , tty , termios

#linux�±�Ҫ�Լ�ʵ��getch()
#���ڻ�ü���������ַ��루������������
        def getch( ) :
            fd = sys.stdin.fileno( )
            old_settings = termios.tcgetattr(fd)
            try :
                tty.setraw( sys.stdin.fileno( ) )
                ch = sys.stdin.read( 1 )
            finally :
                termios.tcsetattr( fd, termios.TCSADRAIN , old_settings )
            return ch
#���������������ʱ����ʾ���ַ�
        def getpass( maskchar = "*" ) :
            password = ""
            while True :
                ch = getch( )
#����س���ʱ���ʾ�������
                if ch == '\r' or ch == '\n' :
                    print ""
                    return password
#�������˸��
                elif ch == '\b' or ord(ch) == 127 :
                    if len(password) > 0 :
                        sys.stdout.write( "\b \b" )
                        password = password[:-1]
#�����ַ�
                else :
                    if maskchar != None :
                        sys.stdout.write( maskchar )
                    password += ch
        return getpass
    elif( Os == 'Windows' ) :
        import msvcrt , sys
        def getpass( maskchar = '*' ) :
            password = ""
            while True :
                ch = msvcrt.getch( )
                if ch in '\r\n' :
                    print ""
                    return password
                elif ch == '\b' :
                    if len( password ) > 0 :
                        sys.stdout.write( '\b \b' )
                        password = password[:-1]
                else :
                    password += ch
                    sys.stdout.write( maskchar )
        return getpass
    else :
        return getpass.getpass

#������
if __name__ == '__main__' :
    print "Enter password : "
    testGetPass = getpass( )
    password = testGetPass( '#' )
#    password = getpass( )
    print password 
