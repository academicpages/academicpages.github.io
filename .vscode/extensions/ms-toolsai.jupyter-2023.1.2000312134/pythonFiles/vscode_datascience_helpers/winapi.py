# This comes from here:
# https://github.com/Pylons/hupper/blob/master/src/hupper/winapi.py
import ctypes
from ctypes import WINFUNCTYPE, wintypes

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

if ctypes.sizeof(ctypes.c_void_p) == 8:
    ULONG_PTR = ctypes.c_int64
else:
    ULONG_PTR = ctypes.c_ulong
BOOL = wintypes.BOOL
DWORD = wintypes.DWORD
HANDLE = wintypes.HANDLE
LARGE_INTEGER = wintypes.LARGE_INTEGER
SIZE_T = ULONG_PTR
ULONGLONG = ctypes.c_uint64
PHANDLER_ROUTINE = WINFUNCTYPE(BOOL, DWORD)

JobObjectAssociateCompletionPortInformation = 7
JobObjectBasicLimitInformation = 2
JobObjectBasicUIRestrictions = 4
JobObjectEndOfJobTimeInformation = 6
JobObjectExtendedLimitInformation = 9
JobObjectSecurityLimitInformation = 5
JobObjectGroupInformation = 11

JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x2000

DELETE = 0x00010000
READ_CONTROL = 0x00020000
SYNCHRONIZE = 0x00100000
WRITE_DAC = 0x00040000
WRITE_OWNER = 0x00080000
STANDARD_RIGHTS_REQUIRED = DELETE | READ_CONTROL | WRITE_DAC | WRITE_OWNER

PROCESS_CREATE_PROCESS = 0x0080
PROCESS_CREATE_THREAD = 0x0002
PROCESS_DUP_HANDLE = 0x0040
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
PROCESS_SET_INFORMATION = 0x0200
PROCESS_SET_QUOTA = 0x0100
PROCESS_SUSPEND_RESUME = 0x0800
PROCESS_TERMINATE = 0x0001
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
PROCESS_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFF

DUPLICATE_SAME_ACCESS = 0x0002

HANDLE_FLAG_INHERIT = 0x0001
HANDLE_FLAG_PROTECT_FROM_CLOSE = 0x0002


class IO_COUNTERS(ctypes.Structure):
    _fields_ = [
        ("ReadOperationCount", ULONGLONG),
        ("WriteOperationCount", ULONGLONG),
        ("OtherOperationCount", ULONGLONG),
        ("ReadTransferCount", ULONGLONG),
        ("WriteTransferCount", ULONGLONG),
        ("OtherTransferCount", ULONGLONG),
    ]


class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("PerProcessUserTimeLimit", LARGE_INTEGER),
        ("PerJobUserTimeLimit", LARGE_INTEGER),
        ("LimitFlags", DWORD),
        ("MinimumWorkingSetSize", SIZE_T),
        ("MaximumWorkingSetSize", SIZE_T),
        ("ActiveProcessLimit", DWORD),
        ("Affinity", ULONG_PTR),
        ("PriorityClass", DWORD),
        ("SchedulingClass", DWORD),
    ]


class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION),
        ("IoInfo", IO_COUNTERS),
        ("ProcessMemoryLimit", SIZE_T),
        ("JobMemoryLimit", SIZE_T),
        ("PeakProcessMemoryUsed", SIZE_T),
        ("PeakJobMemoryUsed", SIZE_T),
    ]


class Handle(HANDLE):
    closed = False

    def Close(self):
        if not self.closed:
            self.closed = True
            CloseHandle(self)

    def Detach(self):
        if not self.closed:
            self.closed = True
            return self.value
        raise ValueError("already closed")

    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, self.value)

    __del__ = Close
    __str__ = __repr__


def CloseHandle(h):
    kernel32.CloseHandle(h)


def CheckError(result, msg):
    if not result:
        raise ctypes.WinError(ctypes.get_last_error(), msg)


def DuplicateHandle(
    hSourceProcess,
    hSourceHandle,
    hTargetProcess,
    desiredAccess,
    inheritHandle,
    options,
):
    targetHandle = wintypes.HANDLE()
    ret = kernel32.DuplicateHandle(
        hSourceProcess,
        hSourceHandle,
        hTargetProcess,
        ctypes.byref(targetHandle),
        desiredAccess,
        inheritHandle,
        options,
    )
    CheckError(ret, "failed to duplicate handle")
    return Handle(targetHandle.value)


def GetCurrentProcess():
    hp = kernel32.GetCurrentProcess()
    return Handle(hp)


def OpenProcess(desiredAccess, inherit, pid):
    hp = kernel32.OpenProcess(desiredAccess, inherit, pid)
    CheckError(hp, "failed to open process")
    return Handle(hp)


def CreateJobObject(jobAttributes, name):
    hp = kernel32.CreateJobObjectA(jobAttributes, name)
    CheckError(hp, "failed to create job object")
    return Handle(hp)


def SetInformationJobObject(hJob, infoType, jobObjectInfo):
    ret = kernel32.SetInformationJobObject(
        hJob,
        infoType,
        ctypes.byref(jobObjectInfo),
        ctypes.sizeof(jobObjectInfo),
    )
    CheckError(ret, "failed to set information job object")


def SetEvent(handle):
    ret = kernel32.SetEvent(handle)
    CheckError(ret, "failed to set event")


def AssignProcessToJobObject(hJob, hProcess):
    ret = kernel32.AssignProcessToJobObject(hJob, hProcess)
    CheckError(ret, "failed to assign process to job object")


def SetHandleInformation(h, dwMask, dwFlags):
    ret = kernel32.SetHandleInformation(h, dwMask, dwFlags)
    CheckError(ret, "failed to set handle information")


CTRL_C_EVENT = 0
CTRL_BREAK_EVENT = 1
CTRL_CLOSE_EVENT = 2
CTRL_LOGOFF_EVENT = 5
CTRL_SHUTDOWN_EVENT = 6


def SetConsoleCtrlHandler(handler, add):
    SetConsoleCtrlHandler = kernel32.SetConsoleCtrlHandler
    SetConsoleCtrlHandler.argtypes = (PHANDLER_ROUTINE, BOOL)
    SetConsoleCtrlHandler.restype = BOOL

    ret = SetConsoleCtrlHandler(handler, add)
    CheckError(ret, "failed in to set console ctrl handler")


def AddConsoleCtrlHandler(handler):
    @PHANDLER_ROUTINE
    def console_handler(ctrl_type):
        if ctrl_type in (
            CTRL_C_EVENT,
            CTRL_BREAK_EVENT,
            CTRL_CLOSE_EVENT,
            CTRL_LOGOFF_EVENT,
            CTRL_SHUTDOWN_EVENT,
        ):
            handler()
            return True
        return False

    SetConsoleCtrlHandler(console_handler, True)
    return lambda: SetConsoleCtrlHandler(console_handler, False)
