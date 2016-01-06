#!/usr/bin/env python_
#-*- coding=utf-8 -*-

import sys , os , subprocess , shlex
from ctypes import *
from sys import platform as _platform
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0


def print_color_test( ) :
    # from ctypes import *
    STD_OUTPUT_HANDLE_ID = c_ulong(0xfffffff5)
    windll.Kernel32.GetStdHandle.restype = c_ulong
    std_output_hdl = windll.Kernel32.GetStdHandle(STD_OUTPUT_HANDLE_ID)
    for color in xrange(16):
        windll.Kernel32.SetConsoleTextAttribute(std_output_hdl, color)
        print "hello : " 
        print color

def print_color( str , color ) :
    if _platform == "win32" :
        STD_OUTPUT_HANDLE_ID = c_ulong(0xfffffff5)
        windll.Kernel32.GetStdHandle.restype = c_ulong
        std_output_hdl = windll.Kernel32.GetStdHandle(STD_OUTPUT_HANDLE_ID)
        windll.Kernel32.SetConsoleTextAttribute(std_output_hdl, color)
        sys.stdout.write( str )
        windll.Kernel32.SetConsoleTextAttribute(std_output_hdl, 7)
    elif _platform == "linux" or _platform == "linux2" or _platform == "cygwin" :
        color_code = {
            "none" : "\033[0m",
            2  : "\033[0;32m" ,
            4  : "\033[0;31m" ,
            6  : "\033[0;33m" ,
            10 : "\033[1;32m" ,
            12 : "\033[1;31m" ,
            14 : "\033[1;33m" ,
        }
        sys.stdout.write( color_code[color] + str + color_code["none"] )
    elif _platform == "darwin" :
        sys.stdout.write( str )
    else :
        sys.stdout.write( str )

def print_green_light( str ) :
    print_color( str , 2 )

def print_red_light( str ) :
    print_color( str , 4 )

def print_yellow_light( str ) :
    print_color( str , 6 ) ;

def print_green( str ) :
    print_color( str , 10 ) 

def print_red( str ) :
    print_color( str , 12 ) 

def print_yellow( str ) :
    print_color( str , 14 ) 

def lexec( cmd ) :
#
#   ִ������
#   �ȵ�����ִ�����֮��
#   �����������������������ִ�н��
#
    print_yellow( "[!] " + cmd + "\n" )
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
    print_yellow( "[!] " + cmd + "\n" )
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
    print ' '
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
        print_green_light( "[+] device found\n" ) ;
        return True
    else :
        print_red( "[-] device not attached ><\n" )
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
        print_green_light( "[+] already root\n" )
        return True
    else :
        print_red( "[-] not root\n" )
        return False

def check_fastboot_mode( ) :
#
#   ��׿�豸����һ������fastbootģʽ�򷵻�True
#   ��׿�豸����һ��������fastbootģʽ�򷵻�False
#
    rc = lexec( "fastboot devices" )
    if rc.strip().find( "fastboot" ) > 0 :
        print_green_light( "[+] fastboot mode\n" )
        return True
    else :
        print_red( "[-] not fastboot mode\n" )
        return False

def root_device( ) :
#
#   ǰ�᣺��׿�豸����һ���Ѿ���debugģʽ
#   ���豸����root
#
    # rc = lexec( "adb root" )
    rc = lexec( "adb vivoroot" )
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
#   ǰ�᣺��׿�豸����һ���Ѿ���debugģʽ
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
            print_green_light( "[+] enter fastboot mode\n" )
            return True
        else :
            print_green_light( "[+] wait for devices : " + try_count + "\n" )
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
                    print_green_light( "[+] log available\n" )
                    return True ;
        print_red( "[-] log not available ><\n" )
        return False
    except IOError :
        print_red( "[-] log file not exist ><\n" )
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
    print_green_light( "\n[+] kill process : " + process_name + "\n" )
    rc = lexec( "adb shell ps | find \"" + process_name + "\"" )
    if rc.strip() == "" :
        print_red( "[-] process " + process_name + " not exist ><" + "\n" )
        return
    kill_cmd = ""
    kill_cmd += "adb shell kill -9" + " "
    kill_cmd += os.popen( "adb shell ps | find \"" + process_name + "\"" ).read().split()[1] + " "
    lexec( kill_cmd )
    return

def push_lib( ) :

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    log_filename = config.get( 'push_lib' , 'log_file' )

    if not check_log( log_filename , "Install:" , 0 , 8 ) :
        exit( "[-] check_log() failed" )

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    if not check_root( ) :
        if not root_device( ) :
            exit( "[-] root_device() failed" )

    logs = read_log( log_filename , "Install:" , 0 , 8 )
    for index , log in enumerate( logs ) :
        cmd_push = 'adb push '
        # cmd_push += os.path.dirname( log_filename ).replace( '\\' , '/' ) + '/'
        cmd_push += log_filename[:log_filename.rfind('/')] + '/'
        cmd_push += log[log.find("out"):].strip() + ' '
        cmd_push += log[log.find("/system"):log.rfind("/")].strip() + " "
        print( "[+] " + str( index + 1 ) + "/" + str( len( logs ) ) + " file(s) :") ;
        lexec_( cmd_push )

def flash_boot( ) :

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    log_filename = config.get( 'flash_boot' , 'log_file' )

    if not check_log( log_filename , "Target boot image:" , 0 , 18 ) :
        exit( "[-] check_log() failed" )

    if not check_fastboot_mode( ) :
        if not check_device( ) :
            exit( "[-] check_device() failed" )
        else :
            if not reboot_fastboot( ) :
                exit( "[-] reboot_fastboot() failed" )

    lexec_( "fastboot bbk unlock_vivo" )

    for log in read_log( log_filename , "Target boot image:" , 0 , 18 ) :
        cmd_flash = "fastboot flash boot "
        # cmd_flash += os.path.dirname( log_filename ).replace( '\\' , '/' ) + '/'
        cmd_flash += log_filename[:log_filename.rfind('/')] + '/'
        cmd_flash += log[log.find("out"):].strip() + " "
        lexec_( cmd_flash )

    lexec_( "fastboot reboot" )

def kill_camera_svr_and_clt( ) :

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    if not check_root( ) :
        if not root_device( ) :
            exit( "[-] root_device() failed" )

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    for process_name in config.get( 'kill_camera_svr_and_clt' , 'camera_process_name' ).split( ' ' ) :
        kill_process( process_name )

def kill_camera_service( ) :

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    if not check_root( ) :
        if not root_device( ) :
            exit( "[-] root_device() failed" )

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    for process_name in config.get( 'kill_camera_service' , 'camera_process_name' ).split( ' ' ) :
        kill_process( process_name )

def kill_camera_client( ) :

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    if not check_root( ) :
        if not root_device( ) :
            exit( "[-] root_device() failed" )

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    for process_name in config.get( 'kill_camera_client' , 'camera_process_name' ).split( ' ' ) :
        kill_process( process_name )

def start_camera( ) :

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    cmd = config.get( "start_camera" , "command" )
    lexec( cmd )

def take_picture( ) :

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    cmd = config.get( "take_picture" , "command" )
    lexec( cmd )

def power_button( ) :

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    cmd = config.get( "power_button" , "command" )
    lexec( cmd )

def unlock_screen( ) :

    # if not check_device( ) :
        # exit( "[-] check_device() failed" )

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    cmd = config.get( "unlock_screen" , "command" )
    lexec( cmd )

def log_fname( ) :

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    print_green( "[+] push_lib   : " + config.get( "push_lib" , "log_file" ) + "\n" )
    print_green( "[+] check_lib  : " + config.get( "check_log" , "log_file" ) + "\n" )
    print_green( "[+] flash_boot : " + config.get( "flash_boot" , "log_file" ) + "\n" )

def check_lib_log( ) :

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    log_filename = config.get( 'push_lib' , 'log_file' )

    if check_log( log_filename , "Install:" , 0 , 8 ) :
        print_green_light( "[+] check lib log success" + "\n" ) ;
    else :
        print_red( "[-] check lib log failed" + "\n" ) ;

def logcat_with_dmesg( ) :

    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    print_yellow( config.get( "logcat_with_dmesg" , "command" ) + "\n" )

def mobicat( ) :
    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    for cmd in config.get ( "mobicat" , "command" ).split( "\"" ) :
        print_yellow( cmd + "\n" )

def metadata( ) :
    config = ConfigParser( ) 
    config.read( os.path.dirname( os.path.realpath( __file__ ) ) + '/qyh.ini' )
    for cmd in config.get ( "metadata" , "command" ).split( "\"" ) :
        print_yellow( cmd + "\n" )

def main_menu( ) :
    sys.stdout.write( ' ' + os.path.basename( sys.argv[0] ) + ' [\n' )
    sys.stdout.write( '           push_lib (' );print_green('pl');sys.stdout.write(')               | \n' )
    sys.stdout.write( '           flash_boot (' );print_green('fb');sys.stdout.write(')             | \n' )
    sys.stdout.write( '           kill_camera_svr_and_clt (' );print_green('kc');sys.stdout.write(')| \n' )
    sys.stdout.write( '           kill_camera_service (' );print_green('kcs');sys.stdout.write(')   | \n' )
    sys.stdout.write( '           kill_camera_client (' );print_green('kcc');sys.stdout.write(')    | \n' )
    sys.stdout.write( '           start_camera (' );print_green('sc');sys.stdout.write(')           | \n' )
    sys.stdout.write( '           take_picture (' );print_green('tp');sys.stdout.write(')           | \n' )
    sys.stdout.write( '           power_button (' );print_green('pb');sys.stdout.write(')           | \n' )
    sys.stdout.write( '           unlock_screen (' );print_green('us');sys.stdout.write(')          | \n' )
    sys.stdout.write( '           log_fname (' );print_green('lf');sys.stdout.write(')              | \n' )
    sys.stdout.write( '           check_lib_log (' );print_green('cll');sys.stdout.write(')         | \n' )
    sys.stdout.write( '           logcat_with_dmesg (' );print_green('ld');sys.stdout.write(')      | \n' )
    sys.stdout.write( '        ]\n' )

if __name__ == "__main__" :
    pass
    if len( sys.argv ) < 2 :
        main_menu( )
    else :
        for arg in sys.argv[1:] :
            if arg == "push_lib" or arg == "pl" :
                push_lib( )
            elif arg == "flash_boot" or arg == "fb" :
                flash_boot( )
            elif arg == "kill_camera_svr_and_clt" or arg == "kc" :
                kill_camera_svr_and_clt( )
            elif arg == "kill_camera_service" or arg == "kcs" :
                kill_camera_service( )
            elif arg == "kill_camera_client" or arg == "kcc" :
                kill_camera_client( )
            elif arg == "start_camera" or arg == "sc" :
                start_camera( )
            elif arg == "take_picture" or arg == "tp" :
                take_picture( )
            elif arg == "power_button" or arg == "pb" :
                power_button( )
            elif arg == "unlock_screen" or arg == "us" :
                unlock_screen( )
            elif arg == "log_fname" or arg == "lf" :
                log_fname( )
            elif arg == "check_lib_log" or arg == "cll" :
                check_lib_log( )
            elif arg == "logcat_with_dmesg" or arg == "ld" :
                logcat_with_dmesg( )
            elif arg == "mobicat" :
                mobicat( )
            elif arg == "metadata" :
                metadata( )
            else :
                main_menu( )





