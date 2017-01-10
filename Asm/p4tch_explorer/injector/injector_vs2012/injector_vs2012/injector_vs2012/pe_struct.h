#include <Windows.h>

/*
typedef struct _IMAGE_DOS_HEADER
{
     WORD e_magic;
     WORD e_cblp;
     WORD e_cp;
     WORD e_crlc;
     WORD e_cparhdr;
     WORD e_minalloc;
     WORD e_maxalloc;
     WORD e_ss;
     WORD e_sp;
     WORD e_csum;
     WORD e_ip;
     WORD e_cs;
     WORD e_lfarlc;
     WORD e_ovno;
     WORD e_res[4];
     WORD e_oemid;
     WORD e_oeminfo;
     WORD e_res2[10];
     LONG e_lfanew;
} IMAGE_DOS_HEADER, *PIMAGE_DOS_HEADER;
*/

typedef struct _NEWPEINF //�ǳ��򱸷ݼӿǺ��PE��Ϣ
{
	LONG  e_lfanew;                //1.��λPE��ǩ��ַ
	WORD  NumberOfSections;        //2.PE�ڼ���
	WORD  SizeOfOptionalHeader;    //3.PE��չͷ��С
	DWORD SizeOfCode;              //4.����IMAGE_SCN_CNT_CODE���Ե����нڵ��ܴ�С
	DWORD SizeOfInitializedData;   //5.�������ѳ�ʼ����������ɵĽڵ��ܴ�С
	DWORD SizeOfUninitializedData; //6.������δ��ʼ����������ɵĽڵ��ܴ�С
	DWORD AddressOfEntryPoint;     //7.������ڣ��ļ������ȱ�ִ�еĴ���ĵ�һ���ֽڵ�RVA
	DWORD BaseOfCode;              //8.���ؽ��ڴ�֮�����ĵ�һ���ֽڵ�RVA
	DWORD ImageBase;               //9.Ԥ���ص�ַ���ļ����ڴ��е���ѡ���ص�ַ
	DWORD SectionAlignment;        //10.�ڴ�ڶ�������
	DWORD FileAlignment;           //11.pe�ڵ��ļ�����ֵ
	DWORD SizeOfImage;             //12.PE�ڴ��е�ӳ��ߴ�
	DWORD SizeOfHeaders;           //13.PE���н�ͷ�ӽڱ�Ĵ�С
	DWORD NumberOfRvaAndSizes;     //14
	IMAGE_DATA_DIRECTORY DataDirectory[16];//15.����Ŀ¼
	DWORD SizeOfRawData;           //16.���н����ļ��ж�����С
}NEWPEINF,*PNEWPEINF;