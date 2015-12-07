#!/usr/bin/env pythoy
# -*- coding: gbk -*-
__author__ = 'QiYunhu-13111020'
'''
    ��������������һ��Whileѭ��
'''
from classes import * ;

#�����ж��ַ�����ߵĹ����ǲ��Ƕ�������
def isNumeric( str ) :
    for i in str :
        if i not in [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ] :
            return False
    return True

#���ڻ�ȡĿ�ĵ�
def destination( ) :
    metro.tips( )
    while True :
        slowPrint( '  Choose a station to go : \n' )
        metro.PrintStationNameList( )
        _input = raw_input( )
        if( _input == '#' ) : 
            return 1
#����Ĳ�������
        while( not isNumeric( _input ) ) :
            metro.tips( )
            slowPrint( '  OOPS! you have to input a number...\n' )
            slowPrint( '        Please input again :\n' )
            metro.PrintStationNameList( )
            _input = raw_input( )
            if( _input == '#' ) : return 1
#��������ֲ��ڿ�ѡ��Χ
        while( int(_input)<1 or int(_input) >35 ) :
            metro.tips( )
            slowPrint( '  OOPS! out of range...\n' )
            slowPrint( '        Please choose again :\n' )
            metro.PrintStationNameList( )
            _input = raw_input( )
            if( _input == '#' ) : return 1
#��������ִ���վ
        while( metro.db.GetStationNameList( )[int(_input)-1] \
            == metro.db.GetThisStationName( ) ) :
            metro.tips( )
            slowPrint( '  OOPS! you chose this station... \n' )
            slowPrint( '        Please choose again :\n' )
            metro.PrintStationNameList( )
            _input = raw_input( )
            if( _input == '#' ) : return 1
        else :
#�����վ����վ�����յ�վ�ͼ۸񱣴浽record��
            metro.record.SetBeginStation( metro.db.GetThisStationName( ) )
            metro.record.SetEndStation( \
                metro.db.GetStationNameList( )[int(_input)-1] )
            metro.record.SetPrice( \
                metro.db.CalcPrice( \
                    metro.db.GetThisStationName( ) ,\
                    metro.db.GetStationNameList( )[int(_input)-1]))
            return 0

#���ڻ��Ͷ���Ǯ����
def money( ) :
    metro.tips( )
    while( True ) :
        slowPrint( '  Insert money : \n' )
        _input = raw_input( )
        if( _input == '#' ) : return 1
#����Ĳ�������
        while( not isNumeric( _input ) ) :
            metro.tips( )
            slowPrint( '  OOPS! you have to input a number...\n' )
            slowPrint( '        Please input again :\n' )
            _input = raw_input( )
            if( _input == '#' ) : return 1
        if( _input == '#' ) : return 1
        else :
            metro.record.SetMoneyGained( int(_input) )
            metro.record.SetMoneyForChange( \
                metro.record.GetMoneyGained( ) - metro.record.GetPrice( ) )
            return 0

#�ж��ǲ���Ҫ��Ʊ
def trans( ) :
#Ͷ���Ǯ�Ҳ�����֧��Ʊ�ۣ��˻��Ѿ�Ͷ���Ǯ��
    if( metro.record.GetMoneyForChange( ) < 0 ) :
        metro.tips( )
        slowPrint( '  You money is not enough for this time...' )
        metro.change( metro.record.GetMoneyGained( ) )
        slowPrint( '  Press any key to go back to main menu\n' )
        raw_input( )
#��Ʊ���㣬�˻��Ѿ�Ͷ���Ǯ��
    elif( metro.db.GetTicketLeft( ) <= 0 ) :
        metro.tips( )
        slowPrint( '  No tickets left .... ' )
        metro.change( metro.record.GetMoneyGained( ) )
        slowPrint( '  Press any key to go back to main menu\n' )
        raw_input( )
#׼����Ʊ
#��ȷ�����ͳ�Ʊ�����ұ��潻�׼�¼
#������'#'����ȡ����Ʊ�������˻��Ѿ�Ͷ���Ǯ��
    else :
        metro.tips( )
        slowPrint( '\n' )
        slowPrint( '  You Insert [ %d ] \n' % metro.record.GetMoneyGained( ) )
        slowPrint( '  for ticket from [ %s ] to [ %s ] \n' % 
                   ( metro.record.GetBeginStation() ,
                     metro.record.GetEndStation() ) )
        check = raw_input( '  Press Enter to continue or \'#\' to go back\n' )
        if( check != '#' ) :
            metro.db.SetTicketLeft( metro.db.GetTicketLeft( ) - 1 )
            metro.tips( )
            metro.printTicket(
                metro.record.GetBeginStation( ) ,
                metro.record.GetEndStation( ) ,
                metro.record.GetPrice( ) )
            metro.change( metro.record.GetMoneyForChange( ) )
            metro.record.SetCompletedTime(
                time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
            metro.db.SaveRecord( metro.record )
            slowPrint( '  Press any key to go back to main menu\n' )
            raw_input( )
        else :
            metro.tips( )
            metro.change( metro.record.GetMoneyGained( ) )
            slowPrint( '  Press any key to go back to main menu\n' )
            raw_input( )

#����Աģʽ
def admin( ) :
    metro.tips( )
    slowPrint( '  Input password : \n  ' )
#��֤�ɹ�
    if( metro.OpenAdminMode( ) ) :
        slowPrint( '  [+] Open success\n' ) 
        slowPrint( '  [+] ' )
        slowPrint( '............',0.05)
        while True :
            metro.adminTips( )
            metro.adminServices( )
            _input = raw_input( )
            if( _input == '#' ) : break 
#��ѯ���׼�¼
            elif( _input == '1' ) :
                metro.adminTips( )
                metro.PrintRecord( )
#�����Ʊ
            elif( _input == '2' ) :
                metro.adminTips( )
                slowPrint( '\n [+] how many ? ' )
                amount = raw_input( )
#���������ӵ�Ʊ����������
                while( not isNumeric( amount ) ) :
                    metro.adminTips( )
                    slowPrint( '  OOPS! you have to input a number...\n' )
                    slowPrint( '        Please input again :\n' )
                    amount = raw_input( )
                    if( amount == '#' ) : break
                if( amount == '#' ) : break
                else :
                    metro.db.SetTicketLeft( 
                        metro.db.GetTicketLeft( ) + int(amount) )
#���ı�վ����
            elif( _input == '3' ) :
                metro.adminTips( )
                metro.PrintStationNameList( )
                slowPrint( '\n [+] select a station as start station :\n' )
                station = raw_input( )
#����Ĵ��Ų�������
                while( not isNumeric( station ) ) :
                    metro.adminTips( )
                    metro.PrintStationNameList( )
                    slowPrint( '  OOPS! you have to input a number...\n' )
                    slowPrint( '        Please input again :\n' )
                    station = raw_input( )
                    if( station == '#' ) : break
                if( station == '#' ) : break
                else :
                    metro.db.SetThisStationName(
                        metro.db.GetStationNameList( )[int(station)-1] )
#��֤ʧ��
    else :
        slowPrint( '  [-] Open fail\n  Press any key to go back' )
        raw_input( )
#��������������Ϣѭ��
if __name__ == '__main__' :
    metro = Metro( )
    while True :
        metro.tips( )
        metro.services( )
        tips_input = raw_input( )
        if( tips_input == '#' ) : 
            metro.cls( )
            break 
        if( tips_input == '1' ) :
            if( destination( ) == 1 ) : continue 
            if( money( ) == 1 ) : continue
            trans( )
        if( tips_input == '2' ) :
            admin( )
