#define kprintf		DbgPrint
#define kmalloc(_s)	ExAllocatePoolWithTag(NonPagedPool, _s, 'SYSQ')
#define kfree(_p)	ExFreePool(_p)

NTSYSAPI NTSTATUS NTAPI ZwQuerySystemInformation 
(
	IN ULONG	SystemInformationClass,
	OUT PVOID	SystemInformation,
	IN ULONG	Length,
	OUT PULONG	ReturnLength
);

void GetKernelModuleBase(char* lpModuleName, ULONG64 *ByRefBase, ULONG *ByRefSize)
{
	typedef struct _SYSTEM_MODULE_INFORMATION_ENTRY
	{
		ULONG Unknow1;
		ULONG Unknow2;
		ULONG Unknow3;
		ULONG Unknow4;
		PVOID Base;
		ULONG Size;
		ULONG Flags;
		USHORT Index;
		USHORT NameLength;
		USHORT LoadCount;
		USHORT ModuleNameOffset;
		char ImageName[256];
	} SYSTEM_MODULE_INFORMATION_ENTRY, *PSYSTEM_MODULE_INFORMATION_ENTRY;
	typedef struct _SYSTEM_MODULE_INFORMATION
	{
		ULONG Count;//�ں����Լ��ص�ģ��ĸ���
		SYSTEM_MODULE_INFORMATION_ENTRY Module[1];
	} SYSTEM_MODULE_INFORMATION, *PSYSTEM_MODULE_INFORMATION;
	typedef struct _KLDR_DATA_TABLE_ENTRY
	{
		LIST_ENTRY64 InLoadOrderLinks;
		ULONG64 __Undefined1;
		ULONG64 __Undefined2;
		ULONG64 __Undefined3;
		ULONG64 NonPagedDebugInfo;
		ULONG64 DllBase;
		ULONG64 EntryPoint;
		ULONG SizeOfImage;
		UNICODE_STRING FullDllName;
		UNICODE_STRING BaseDllName;
		ULONG   Flags;
		USHORT  LoadCount;
		USHORT  __Undefined5;
		ULONG64 __Undefined6;
		ULONG   CheckSum;
		ULONG   __padding1;
		ULONG   TimeDateStamp;
		ULONG   __padding2;
	}KLDR_DATA_TABLE_ENTRY, *PKLDR_DATA_TABLE_ENTRY;
    ULONG NeedSize, i, ModuleCount, BufferSize = 0x5000;
    PVOID pBuffer = NULL;
	PCHAR pDrvName = NULL;
    NTSTATUS Result;
    PSYSTEM_MODULE_INFORMATION pSystemModuleInformation;
    do
    {
        //�����ڴ�
        pBuffer = kmalloc( BufferSize );
        if( pBuffer == NULL )
            return;
        //��ѯģ����Ϣ
        Result = ZwQuerySystemInformation( 11, pBuffer, BufferSize, &NeedSize );
        if( Result == STATUS_INFO_LENGTH_MISMATCH )
        {
            kfree( pBuffer );
            BufferSize *= 2;
        }
        else if( !NT_SUCCESS(Result) )
        {
            //��ѯʧ�����˳�
            kfree( pBuffer );
            return;
        }
    }
    while( Result == STATUS_INFO_LENGTH_MISMATCH );
    pSystemModuleInformation = (PSYSTEM_MODULE_INFORMATION)pBuffer;
	//���ģ���������
    ModuleCount = pSystemModuleInformation->Count;
	//�������е�ģ��
    for( i = 0; i < ModuleCount; i++ )
	{
		if((ULONG64)(pSystemModuleInformation->Module[i].Base) > (ULONG64)0x8000000000000000)
		{
			pDrvName = pSystemModuleInformation->Module[i].ImageName+pSystemModuleInformation->Module[i].ModuleNameOffset;
			if( _stricmp(pDrvName,lpModuleName)==0 )
			{
				*ByRefBase = (ULONG64)pSystemModuleInformation->Module[i].Base;
				*ByRefSize = pSystemModuleInformation->Module[i].Size;
				goto exit_sub;
			}
		}
	}
exit_sub:
	kfree(pBuffer);
}

