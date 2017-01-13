#include <ntddk.h>

#define dprintf				DbgPrint

#define	DEVICE_NAME			L"\\Device\\hookssdt_x64"
#define LINK_NAME			L"\\DosDevices\\hookssdt_x64"
#define LINK_GLOBAL_NAME	L"\\DosDevices\\Global\\hookssdt_x64"

#define IOCTL_ULR3IN 	CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS) //In LONG
#define IOCTL_USR3IN 	CTL_CODE(FILE_DEVICE_UNKNOWN, 0x801, METHOD_BUFFERED, FILE_ANY_ACCESS) //In BSTR
#define IOCTL_GetKPEB 	CTL_CODE(FILE_DEVICE_UNKNOWN, 0x802, METHOD_BUFFERED, FILE_ANY_ACCESS) //Out LONG
#define IOCTL_GetBSTR 	CTL_CODE(FILE_DEVICE_UNKNOWN, 0x804, METHOD_BUFFERED, FILE_ANY_ACCESS) //Out BSTR
#define IOCTL_ReInline	CTL_CODE(FILE_DEVICE_UNKNOWN, 0x803, METHOD_BUFFERED, FILE_ANY_ACCESS) //Test Call Only
#define IOCTL_Struct	CTL_CODE(FILE_DEVICE_UNKNOWN, 0x805, METHOD_BUFFERED, FILE_ANY_ACCESS) //I+O Struct