VERSION 5.00
Begin VB.Form frm_Main 
   BorderStyle     =   1  'Fixed Single
   ClientHeight    =   735
   ClientLeft      =   45
   ClientTop       =   345
   ClientWidth     =   5415
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   735
   ScaleWidth      =   5415
   StartUpPosition =   2  '��Ļ����
   Begin VB.CommandButton Command7 
      Caption         =   "HOOK"
      Height          =   495
      Left            =   1440
      TabIndex        =   1
      Top             =   120
      Width           =   1215
   End
   Begin VB.CommandButton Command6 
      Caption         =   "UNHOOK"
      Height          =   495
      Left            =   2760
      TabIndex        =   2
      Top             =   120
      Width           =   1215
   End
   Begin VB.CommandButton Command4 
      Caption         =   "ж����"
      Height          =   495
      Left            =   4080
      TabIndex        =   3
      Top             =   120
      Width           =   1215
   End
   Begin VB.CommandButton Command3 
      Caption         =   "������"
      Height          =   495
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   1215
   End
End
Attribute VB_Name = "frm_Main"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub Command3_Click()
    With DrvController
        .InstDrv
        .StartDrv
        .OpenDrv
    End With
    If DrvController.OpenDrv = False Then MsgBox "��������ʧ��", 64, ""
    If DrvController.OpenDrv = True Then Command3.Enabled = False
End Sub

Private Sub Command4_Click()
    With DrvController
        .StopDrv
        .DelDrv
    End With
    Command3.Enabled = True
End Sub

Private Sub Command6_Click()
    UNHOOK_SSSDT
    Command6.Enabled = False
End Sub

Private Sub Command7_Click()
    HOOK_SSSDT
    Command7.Enabled = False
End Sub

Private Sub Form_Load()
    'load and inst drv
    With DrvController
        .szDrvFilePath = Replace(App.Path & "\Fuck3SDT.sys", "\\", "\")
        .szDrvLinkName = "Fuck3SDT"
        .szDrvDisplayName = "Fuck3SDT"
        .szDrvSvcName = "Fuck3SDT"
    End With
    Me.Caption = "Hook NtUserPostMessage x64 - PID=" & CStr(GetCurrentProcessId)
End Sub

Private Sub Form_Unload(cancel As Integer)
    If Command7.Enabled = False Then
        Call Command6_Click
    End If
    With DrvController
        .StopDrv
        .DelDrv
    End With
End Sub
