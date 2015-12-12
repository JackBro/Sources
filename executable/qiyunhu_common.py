#!/usr/bin/env python_
#-*- coding=utf-8 -*-

#
#   �󲿷���ʹ��adb/fastboot�õ��ĺ���
#
import sys , os , subprocess , shlex

def lexec( cmd ) :
#
#   ִ������
#   �ȵ�����ִ�����֮��
#   �����������������������ִ�н��
#
    print "[!] " + cmd
    rc = os.popen( cmd ).read( )
    print rc
    return rc

def lexec_( cmd ) :
#
#   ִ������
#   ʵʱ�����������
#   �ȵ�����ִ�����֮��
#   �ٷ�������ִ�н��
#
    print "[*] " + cmd
    rc = ""
    process = subprocess.Popen( shlex.split( cmd ), stdout=subprocess.PIPE )
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            rc += output
            print "[+] " + output.strip()
    # rc = process.poll()
    return rc

def check_device( ) :
#
#   ���Ұ�׿�豸����һ��
#   ��ȷ���Ƿ��debugģʽ��
#
#   �ҵ��Ѿ���debugģʽ���豸ʱ����True
#   û�ҵ�����False
#
    rc = lexec( "adb devices" )
    if rc.strip().replace( "devices" , "" ).find( "device" ) > 0 :
        return True
    else :
        print "[-] device not attached ><\n"
        return False

def check_root( ) :
#
#   ǰ�᣺��׿�豸����һ���Ѿ���debugģʽ
#   ȷ���Ƿ��Ѿ�root
#
#   �Ѿ�root����True
#   û��root����False
#
    rc = lexec ( "adb remount" ) 
    if rc.find( "succeeded" ) > 0 :
        print "[+] already root\n"
        return True
    else :
        print "[-] not root\n"
        return False

def check_fastboot_mode( ) :
#
#   ��׿�豸����һ������fastbootģʽ�򷵻�True
#   ��׿�豸����һ��������fastbootģʽ�򷵻�False
#
    rc = lexec( "fastboot devices" )
    if rc.strip().find( "fastboot" ) > 0 :
        print "[+] fastboot mode\n"
        return True
    else :
        print "[-] not fastboot mode\n"
        return False

def root_device( ) :
#
#   ǰ�᣺��׿�豸����һ���Ѿ���debugģʽ
#   ���豸����root
#
    rc = lexec( "adb root" )
    if rc.strip().find( "as root" ) > 0 :
        return True
    else :
        rc = lexec( "adb vivoroot" )
        if rc.strip().find( "as root" ) > 0 :
            return True
        else :
            return False
 
def reboot_fastboot( ) :    
#
#   ǰ�᣺��׿�豸����һ���Ѿ���debugģʽ����root
#
#   ���Խ���fastbootģʽ
#   ����ɹ�����True
#   ����ʧ�ܷ���False
#   
    lexec( "adb reboot bootloader" )
    try_count = 14
    while( try_count > 0 ) :
        rc = lexec( "fastboot devices" ) ;
        if rc.find( "fastboot" ) :
            print "[+] enter fastboot mode\n"
            return True
        else :
            print "[+] wait for devices : " + try_count
            try_count -= 1
    # lexec( "fastboot continue" )
    return False

def check_log( log_filename , keyword , k_index_start , k_index_end ) :
#
#   ����ȷ��log�ļ��Ƿ����
#   ����log�ļ��в����Ƿ��а���keyword���У�log�Ƿ���Ч��
#   
#   log_filename    :   log�ļ���
#   keyword         :   ��¼�Ĺؼ���
#   k_index_start   :   keyword��ÿһ�г��ֵ���ʼλ��
#   k_index_end     :   keyword��ÿһ�г��ֵĽ���λ��
#
#   log��Ч����True
#   log��Ч����False
#
    try :
        with open( log_filename , 'r' ) as f :
            for line in f.readlines( ) :
                if line[k_index_start:k_index_end] == keyword :
                    print "[+] log available\n"
                    return True ;
        print "[+] log not available ><\n"
        return False
    except IOError :
        print "[-] log file not exist ><\n"
        return False

def read_log( log_filename , keyword , k_index_start , k_index_end ) :
#
#   ��log�ļ��в��Һ���keyword����
#   
#   log_filename    :   log�ļ���
#   keyword         :   ��¼�Ĺؼ���
#   k_index_start   :   keyword��ÿһ�г��ֵ���ʼλ��
#   k_index_end     :   keyword��ÿһ�г��ֵĽ���λ��
#
#   ����ֵlog_list��Ϊlog�ļ���keywordλ����ȷ��ÿһ��
#
    log_list = []
    with open( log_filename , 'r' ) as f :
        for line in f.readlines( ) :
            if line[k_index_start:k_index_end] == keyword :
                log_list.append( line.strip() )
    return log_list

def kill_process( process_name ) :
#
#   ǰ�᣺��׿�豸����һ���Ѿ���debugģʽ����root
#   ps֮����ҽ�����������
#
    print "\n\n[+] kill camera serivce : "
    rc = lexec( "adb shell ps | grep " + process_name )
    if rc.strip() == "" :
        print "[-] process " + process_name + " not exist ><"
        return
    kill_cmd = ""
    kill_cmd += "adb shell kill -9" + " "
    kill_cmd += os.popen( "adb shell ps | grep " + process_name + " | gawk '{print $2}'" ).read( ) + " "
    lexec( kill_cmd )
    return

def kill_camera_service( ) :
    kill_process( "org.codeaurora.snapcam" )
    kill_process( "com.android.camera" )
    kill_process( "mm-qcamera-daemon" )

if __name__ == "__main__" :
    # if reboot_fastboot( ) :
        # print True
    # else :
        # print False
    pass























