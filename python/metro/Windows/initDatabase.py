#!/usr/bin/env python
#-*- coding: gbk -*-
__author__ = 'QiYunhu-13111020'
'''
    ���ڳ�ʼ�����ݿ�
    price.xls�ǴӰٶ��ҵ������������۸��
    �򵥵ش���߶���������sqlite3�洢��metro.db��METROPRICE����
    CONTEXT�����ڱ�����Ʊ�����ͱ�վ����
        Ĭ�ϱ�վΪ'Сկ'����Ʊ2��
    SELLINGRECORD�����ڱ��潻�׼�¼
                            2014-11-25
'''
import xlrd , sqlite3, platform

#linux������ʹ��utf-8���������������
#windows������ʹ��gbk����
Os = platform.system( )
if( Os == 'Linux' ) :
    CODING = 'utf-8'
elif( Os == 'Windows' ) :
    CODING = 'gbk'


fname = "price.xls"
#��ȡexcelָ��
bk = xlrd.open_workbook( fname )
shxrange = range( bk.nsheets )
#�򿪹�����
try :
    sh = bk.sheet_by_name( "Sheet1" )
except :
    print "No sheet in %s named Sheet1" % fname
#��ȡ����������
nrows = sh.nrows
ncols = sh.ncols
#����val���ڴ���METROPRICE��
val = []
#��������վ����
names = sh.row_values( 1 )
for i in range( 2 , nrows - 1 ) :
    for j in range( 3 , ncols ) :
        start = sh.row_values( i )[ 2 ]
        end = names[ j ]
        price = sh.row_values( i )[ j ] 
        val.append( [ start.encode( CODING ) , end.encode( CODING ) , price if price != '-' else 0 ] )

#�����ݿ�
conn = sqlite3.connect( 'metro.db' )
#windows��ʹ��gbk����
conn.text_factory = lambda x: unicode( x , CODING , "ignore" ) 
#��ȡ�α�
cursor = conn.cursor( )
#��METROPRICE��
cursor.execute( "DROP TABLE IF EXISTS METROPRICE" )
cursor.execute( "CREATE TABLE METROPRICE (\
                    START VARCHAR( 30 ) ,\
                    END VARCHAR( 30 ) ,\
                    PRICE INT )" )
sql = '''INSERT INTO METROPRICE VALUES( ? , ? , ? )'''
#��������
cursor.executemany( sql , tuple( val ) )

#��CONTEXT��
#Ĭ�����վ����վ��ΪСկ
#Ĭ����Ʊ������
cursor.execute( "DROP TABLE IF EXISTS CONTEXT" )
cursor.execute( "CREATE TABLE CONTEXT( NAME VARCHAR(30), NUM_VALUE INT , STR_VALUE VARCHAR  )" )
cursor.execute( "INSERT INTO CONTEXT( NAME , NUM_VALUE ) \
                 VALUES ( 'TICKETS' , 2 )" )
cursor.execute( "INSERT INTO CONTEXT( NAME , STR_VALUE ) \
                 VALUES ( 'THIS_STATION' , 'Сկ' )" )

#��SELLINGRECORD��
cursor.execute( "DROP TABLE IF EXISTS SELLINGRECORD" )
cursor.execute( "CREATE TABLE SELLINGRECORD(\
                    ID INTEGER PRIMARY KEY,\
                    RECORD VARCHAR)" )
cursor.close( )
conn.commit( )
conn.close( )
