#!/usr/bin/env python_
#-*- coding=utf-8 -*-

#
# ��������֮������ʾ Target boot image: out
# ���������ʾ��push���ļ�
#

import qiyunhu_common
from qiyunhu_common import * ;

log_filename = "compile_boot.log"

def flash_boot( log_list ) :
    for log in log_list :
        flash_cmd = "fastboot flash boot "
        flash_cmd += log[log.find("out"):].strip() + " "
        print flash_cmd
        lexec( flash_cmd )
    return
    
if __name__ == "__main__" :

    if not check_log( log_filename , "Target boot image:" , 0 , 18 ) :
        exit( "[-] check_log() failed" )

    if not check_device( ) :
        exit( "[-] check_device() failed" )

    if not check_fastboot_mode( ) :
        if check_root( ) :
            if not reboot_fastboot( ) :
                exit( "[-] reboot_fastboot() failed" )
        else :
            if root_device( ) :
                if not reboot_fastboot( ) :
                    exit( "[-] reboot_fastboot() failed" )
            else :
                exit( "[-] root_device() failed" )

    flash_boot( read_log( log_filename , "Target boot image:" , 0 , 18 ) )
    lexec( "fastboot reboot" )





