#!/usr/bin/env pythoy
# -*- coding: gbk -*-
__author__ = 'QiYunhu-13111020'
'''
    ������ Metro SellingRecord dbOperator
        Metro�������Ʊ����Ҫ��ʵ�ֵĹ���
        SellingRecord��������װÿ�γɹ�����֮��Ľ�������
        dbOperator����ʵ�ֺ����ݿ��йصĲ���

                            2014-12-14
'''

import sqlite3 , time , platform , os , getpass
from slowPrint import slowPrint

global ADMINPASSWORD
ADMINPASSWORD = "admin"

#linux������ʹ��utf-8���������������
#windows������ʹ��gbk����
Os = platform.system( )
if( Os == 'Linux' ) :
    CODING = 'utf-8'
elif( Os == 'Windows' ) :
    CODING = 'gbk'
else :
    CODING = 'utf-8'


class Metro :

#��ʼ������
    def __init__( self ) :
        self.db = dbOperator( )
        self.record = SellingRecord( )

#ʵ����������
    def cls( self ) :
        Os = platform.system( )
        if( Os == 'Linux' ) :
            os.system( 'clear' )
        if( Os == 'Windows' ) :
            os.system( 'cls' )

#�����ӭ��Ϣ
    def tips( self ) :
        self.cls( )
        slowPrint( '\n' ) 
        slowPrint( ' Welcome! \n' ) 
        slowPrint( ' This station is [ %s ] \n' % self.db.GetThisStationName( )  )
        slowPrint( ' This machine has [ %d ] tickets now\n' % self.db.GetTicketLeft( ) )
        slowPrint( ' Today is %s \n' % ( time.strftime( "%Y-%m-%d" , time.localtime( time.time() ) ) ) )
        slowPrint( ' You can go back by inputing \'#\' at any time\n' )
        slowPrint( '\n' )

#����Աģʽ�Ļ�ӭ��Ϣ
    def adminTips( self ) :
        self.cls( )
        slowPrint( '\n' ) 
        slowPrint( ' [+] Welcome! \n' ) 
        slowPrint( ' [+] This station is [ %s ] \n' % self.db.GetThisStationName( )  )
        slowPrint( ' [+] This machine has [ %d ] tickets now\n' % self.db.GetTicketLeft( ) )
        slowPrint( ' [+] Today is %s \n' % ( time.strftime( "%Y-%m-%d" , time.localtime( time.time() ) ) ) )
        slowPrint( ' [+] You can go back by inputing \'#\' at any time\n' )
        slowPrint( ' [+]  Careful! This is administrate mode\n' )
        slowPrint( '\n' )

#��ѡ�Ĳ���
    def services( self ) :
        slowPrint( '\n' ) 
        slowPrint( '   Services : \n' )
        slowPrint( '\n' )
        slowPrint( '    1. Buy metro ticket\n' )
        slowPrint( '    2. Manager this mechine\n' )    

#����Ա��ѡ�Ĳ���
    def adminServices( self ) :
        slowPrint( '\n' )
        slowPrint( ' [+]  Services : \n' )
        slowPrint( '\n' )
        slowPrint( ' [+]   1. Print Selling Record\n' )
        slowPrint( ' [+]   2. Add tickets to this machine\n' )    
        slowPrint( ' [+]   3. Change this station name\n' )

#��Ǯ������Ǯ
    def change( self , money ) :
        slowPrint( '\n' )
        slowPrint( '----------------------------------------------------\n' )
        slowPrint( '  This is your money for change/refund : [ %d ]\n' % money )
        slowPrint( '----------------------------------------------------\n' )
        slowPrint( '\n' )

#��Ʊ
    def printTicket( self , begin , end , price ) :
        slowPrint( '\n' )
        slowPrint( '  This is your ticket , have a nice trip \n' )
        slowPrint( '\n' )
        slowPrint( '  +--------------------------------------+ \n' )
        slowPrint( '  |            Metro Ticket              | \n' )
        slowPrint( '  +--------------------------------------+ \n' )
        slowPrint( '  |  %s -> %s \n' % ( begin , end ) )
        slowPrint( '  |  price : %d                           |\n' % price )
        slowPrint( '  +--------------------------------------+ \n' )

#��ӡ��ѡ���վ��
    def PrintStationNameList( self ) :
        nameList = self.db.GetStationNameList( )
        index = 0 ;
        while( index < nameList.__len__( ) ) :
            if( index % 4 == 0 ) :
                if( index + 4 < nameList.__len__( ) ) :
                    slowPrint( '\n    %2d ~ %2d : ' % ( index + 1 , index + 4 ) , 0.00025 )
                else :
                    slowPrint( '\n    %02d ~ %02d : ' % ( index + 1 , nameList.__len__( ) ) , 0.00025 )
            slowPrint( '%s  ' % nameList[index] , 0.00025 )
            index = index + 1 
        slowPrint( '\n' )

#��ӡ��ʷ���׼�¼
#ÿ��ӡ������ͣһ�·�ֹ����̫�࿴�����ϱߵ���Ϣ
    def PrintRecord( self ) :
        recordList = self.db.GetRecord( )
        index = 0 
        while( index < recordList.__len__() ) :
            slowPrint( ' ' , 0.05 )
            print( recordList[index] )
            if( ( index + 1 ) % 7 == 0 ) :
                input_ = raw_input( '\nEnter to continue, input \'#\' to stop' )
                if( input_ == '#' ) : break
            index = index + 1 
        input_ = raw_input( '\n...END Press any key to go back' )

#�������Աģʽ��ʱ����������֤
#Ĭ������admin
    def OpenAdminMode( self ) :
        getPass = getpass.getpass( )
        password = getPass( "#" )
        if( password == ADMINPASSWORD ) :
            return True
        return False
        
#���ڴ洢�ɹ��Ľ��׼�¼
class SellingRecord :
#���վ����վ���ķ�������������
    def SetBeginStation( self , begin ) :
        self.__beginStation = begin
    def GetBeginStation( self ) :
        return self.__beginStation
#�յ�վ�ķ�������������
    def SetEndStation( self , end ) :
        self.__endStation = end
    def GetEndStation( self ) :
        return self.__endStation
#Ͷ��Ǯ�ҵķ�������������
    def SetMoneyGained( self , money ) :
        self.__moneyGained = money
    def GetMoneyGained( self ) :
        return self.__moneyGained
#Ʊ�۵ķ�������������
    def SetPrice( self , price ) :
        self.__price = price
    def GetPrice( self ) :
        return self.__price
#Ӧ����Ǯ�ķ�������������
    def SetMoneyForChange( self , money ) :
        self.__moneyForChange = money
    def GetMoneyForChange( self ) :
        return self.__moneyForChange
#��ɽ��׵�ʱ��������
    def SetCompletedTime( self , time ) :
        self.__completedTime = time 
#�൱��java��toString()����
    def __str__( self ) :
        return ' %s price:%-3d gain:%-3d change:%-3d %s -> %s' % \
            ( self.__completedTime , self.__price , self.__moneyGained , 
              self.__moneyForChange , self.__beginStation , self.__endStation )

class dbOperator :

#���캯����������ݿ����Ӻ��α�
    def __init__( self ) :
        self.__conn = sqlite3.connect( 'metro.db' )
        self.__conn.text_factory = lambda x: unicode( x , CODING , "ignore" ) 
        self.__cursor = self.__conn.cursor( )

#�����������ر��α�����ݿ�����
    def __del__( self ) :
        self.__cursor.close( )
        self.__conn.close( )
        
#�����ú���
    def test( self ) :
        self.__cursor.execute( "select * from METROPRICE\
                                where start = 'Сկ' \
                                limit 0 , 5 " )
        str = self.__cursor.fetchall( )
        for i in str :
            for j in i :
                print j 
            print( "----" )

#�������վ������֣�����һ��List
    def GetStationNameList( self ) :
        self.__cursor.execute( "select distinct start \
                                from METROPRICE" ) 
        tmp = self.__cursor.fetchall( ) 
        r = []
        for i in tmp :
            r.append( i[0].encode( CODING ) )
        return r

#���������վ����վ�����յ�վ������
#����ֵ��Ʊ��
    def CalcPrice( self , begin , end ) :
        self.__cursor.execute( "select * from METROPRICE\
                                where start = ? and end = ?",
                                ( begin , end ) )
        return self.__cursor.fetchall( )[0][2]

#���ñ�����ʣ��Ʊ����
    def SetTicketLeft( self , ti ) :
        self.__cursor.execute( "update CONTEXT \
                                set NUM_VALUE = ?\
                                where name = 'TICKETS'" , (ti,) )
        self.__conn.commit( )

#��ñ�����ʣ���Ʊ��
    def GetTicketLeft( self ) :
        self.__cursor.execute( "select NUM_VALUE from CONTEXT\
                                where NAME = 'TICKETS'" )
        return self.__cursor.fetchall( )[0][0]

#���ñ�վ����
    def SetThisStationName( self , name ) :
        self.__cursor.execute( "update CONTEXT\
                                set STR_VALUE = ?\
                                where name = 'THIS_STATION'" , (name,) )
        self.__conn.commit( )

#��ñ�վ����
    def GetThisStationName( self ) :
        self.__cursor.execute( "select STR_VALUE from CONTEXT\
                                where name = 'THIS_STATION'" )
        return self.__cursor.fetchall( )[0][0].encode( CODING )

#���潻�׼�¼
#���򻯳ɱ����ַ���������
    def SaveRecord( self , record ) :
        self.__cursor.execute( "INSERT INTO SELLINGRECORD( RECORD ) VALUES ( ? )" , (record.__str__(),) )
        self.__conn.commit( )

#��ý��׼�¼
#����ֵ��һ��List
    def GetRecord( self ) :
        self.__cursor.execute( "SELECT RECORD FROM SELLINGRECORD" )
        tmp = self.__cursor.fetchall( )
        r = []
        for i in tmp :
            r.append( i[0] )
        return r

#������
if __name__ == '__main__' :
    a = dbOperator( )
    # a.test( )
    # a.SetTicketLeft( 2 )
    # print a.GetTicketLeft( )
    # a.SetTicketLeft( 4 )
    # print a.GetTicketLeft( )
    # print a.CalcPrice( 'Сկ' , 'Сկ' )
    # a.SetThisStationName( '����·' ) 
    # print a.GetThisStationName( )
    # a.SetThisStationName( 'Сկ' ) 
    # print a.GetThisStationName( )
    # for i in a.GetStationNameList( ) :
        # print i 
    # metro = Metro( )
    # metro.PrintStationNameList( )
