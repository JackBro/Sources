/* overflow :
 *
 * using debug in visual studio to see the overflow position in string s in function main
 * using function printf to see the position of function test 
 * replace the overflow position with the position of funtion test
 *
 * 2013-6-7 22:47:50 writen
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void jump ( const char * s )
{
    char buf[10] ;
    strcpy ( buf , s ) ;
    return ;
}

void test ( void ) 
{
    puts ( "\n\t\t\t\t\t\t Wass up ! " ) ;
    system ( "pause>nul" ) ;
    exit ( 0 ) ;
}
/*
 * aaa 0040116C aaa
 * ��ʾ����test�ĵ�ַ�� 0x0040116C
 * �������ַ��Ϊ�����ַ����������
 * һ����char s[50] ��ߵ� \x6C\x11\x40\x00 (ע��˳�򵹹�����)
 * ����һ�����±ߵ� s[16] = һֱ�� s[19] = �ľ�
 * ���е�ֵ��6c 11 40 00��16����ת����ʮ���Ƶ�ֵ
 * ˳��Ҳ��������
 *
 */
int main()
{
    char s[50] = "abcdefghijklmnop\x6C\x11\x40\x00" ;
    printf ( " \n\taaa %p aaa\n" , test ) ;
    /*
    s[16] = 108 ;
    s[17] = 17 ;
    s[18] = 64 ;
    s[19] = 00 ;
    */
    jump ( s ) ;
    system ( "pause>nul" ) ;
    return 0 ;
}