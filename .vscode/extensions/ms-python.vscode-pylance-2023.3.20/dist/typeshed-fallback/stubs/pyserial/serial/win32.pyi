import sys
from ctypes import Structure, Union, _CField, _NamedFuncPointer, _Pointer, c_int64, c_ulong, c_void_p
from ctypes.wintypes import DWORD
from typing_extensions import TypeAlias

if sys.platform == "win32":
    def is_64bit() -> bool: ...

    ULONG_PTR: type[c_int64 | c_ulong]

    class _SECURITY_ATTRIBUTES(Structure):
        nLength: _CField
        lpSecurityDescriptor: _CField
        bInheritHandle: _CField
    LPSECURITY_ATTRIBUTES: type[_Pointer[_SECURITY_ATTRIBUTES]]
    CreateEvent: _NamedFuncPointer
    CreateFile: _NamedFuncPointer
    # The following are included in __all__ but their existence is not guaranteed as
    # they are defined in a try/except block. Their aliases above are always defined.
    CreateEventW: _NamedFuncPointer
    CreateFileW: _NamedFuncPointer

    class _OVERLAPPED(Structure):
        Internal: _CField
        InternalHigh: _CField
        Offset: _CField
        OffsetHigh: _CField
        Pointer: _CField
        hEvent: _CField
    OVERLAPPED: TypeAlias = _OVERLAPPED

    class _COMSTAT(Structure):
        fCtsHold: _CField
        fDsrHold: _CField
        fRlsdHold: _CField
        fXoffHold: _CField
        fXoffSent: _CField
        fEof: _CField
        fTxim: _CField
        fReserved: _CField
        cbInQue: _CField
        cbOutQue: _CField
    COMSTAT: TypeAlias = _COMSTAT

    class _DCB(Structure):
        DCBlength: _CField
        BaudRate: _CField
        fBinary: _CField
        fParity: _CField
        fOutxCtsFlow: _CField
        fOutxDsrFlow: _CField
        fDtrControl: _CField
        fDsrSensitivity: _CField
        fTXContinueOnXoff: _CField
        fOutX: _CField
        fInX: _CField
        fErrorChar: _CField
        fNull: _CField
        fRtsControl: _CField
        fAbortOnError: _CField
        fDummy2: _CField
        wReserved: _CField
        XonLim: _CField
        XoffLim: _CField
        ByteSize: _CField
        Parity: _CField
        StopBits: _CField
        XonChar: _CField
        XoffChar: _CField
        ErrorChar: _CField
        EofChar: _CField
        EvtChar: _CField
        wReserved1: _CField
    DCB: TypeAlias = _DCB

    class _COMMTIMEOUTS(Structure):
        ReadIntervalTimeout: _CField
        ReadTotalTimeoutMultiplier: _CField
        ReadTotalTimeoutConstant: _CField
        WriteTotalTimeoutMultiplier: _CField
        WriteTotalTimeoutConstant: _CField
    COMMTIMEOUTS: TypeAlias = _COMMTIMEOUTS

    GetLastError: _NamedFuncPointer
    LPOVERLAPPED: type[_Pointer[_OVERLAPPED]]
    LPDWORD: type[_Pointer[DWORD]]
    GetOverlappedResult: _NamedFuncPointer
    ResetEvent: _NamedFuncPointer
    LPCVOID = c_void_p
    WriteFile: _NamedFuncPointer
    LPVOID = c_void_p
    ReadFile: _NamedFuncPointer
    CloseHandle: _NamedFuncPointer
    ClearCommBreak: _NamedFuncPointer
    LPCOMSTAT: type[_Pointer[_COMSTAT]]
    ClearCommError: _NamedFuncPointer
    SetupComm: _NamedFuncPointer
    EscapeCommFunction: _NamedFuncPointer
    GetCommModemStatus: _NamedFuncPointer
    LPDCB: type[_Pointer[_DCB]]
    GetCommState: _NamedFuncPointer
    LPCOMMTIMEOUTS: type[_Pointer[_COMMTIMEOUTS]]
    GetCommTimeouts: _NamedFuncPointer
    PurgeComm: _NamedFuncPointer
    SetCommBreak: _NamedFuncPointer
    SetCommMask: _NamedFuncPointer
    SetCommState: _NamedFuncPointer
    SetCommTimeouts: _NamedFuncPointer
    WaitForSingleObject: _NamedFuncPointer
    WaitCommEvent: _NamedFuncPointer
    CancelIoEx: _NamedFuncPointer

    ONESTOPBIT: int
    TWOSTOPBITS: int
    NOPARITY: int
    ODDPARITY: int
    EVENPARITY: int
    RTS_CONTROL_HANDSHAKE: int
    RTS_CONTROL_ENABLE: int
    DTR_CONTROL_HANDSHAKE: int
    DTR_CONTROL_ENABLE: int
    MS_DSR_ON: int
    EV_RING: int
    EV_PERR: int
    EV_ERR: int
    SETXOFF: int
    EV_RXCHAR: int
    GENERIC_WRITE: int
    PURGE_TXCLEAR: int
    FILE_FLAG_OVERLAPPED: int
    EV_DSR: int
    MAXDWORD: int
    EV_RLSD: int
    ERROR_IO_PENDING: int
    MS_CTS_ON: int
    EV_EVENT1: int
    EV_RX80FULL: int
    PURGE_RXABORT: int
    FILE_ATTRIBUTE_NORMAL: int
    PURGE_TXABORT: int
    SETXON: int
    OPEN_EXISTING: int
    MS_RING_ON: int
    EV_TXEMPTY: int
    EV_RXFLAG: int
    MS_RLSD_ON: int
    GENERIC_READ: int
    EV_EVENT2: int
    EV_CTS: int
    EV_BREAK: int
    PURGE_RXCLEAR: int

    class N11_OVERLAPPED4DOLLAR_48E(Union):
        Offset: _CField
        OffsetHigh: _CField
        Pointer: _CField

    class N11_OVERLAPPED4DOLLAR_484DOLLAR_49E(Structure):
        Offset: _CField
        OffsetHigh: _CField
    PVOID: TypeAlias = c_void_p
