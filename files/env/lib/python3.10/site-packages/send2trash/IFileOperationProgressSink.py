# Sample implementation of IFileOperationProgressSink that just prints
# some basic info

import pythoncom
from win32com.shell import shell, shellcon
from win32com.server.policy import DesignatedWrapPolicy


class FileOperationProgressSink(DesignatedWrapPolicy):
    _com_interfaces_ = [shell.IID_IFileOperationProgressSink]
    _public_methods_ = [
        "StartOperations",
        "FinishOperations",
        "PreRenameItem",
        "PostRenameItem",
        "PreMoveItem",
        "PostMoveItem",
        "PreCopyItem",
        "PostCopyItem",
        "PreDeleteItem",
        "PostDeleteItem",
        "PreNewItem",
        "PostNewItem",
        "UpdateProgress",
        "ResetTimer",
        "PauseTimer",
        "ResumeTimer",
    ]

    def __init__(self):
        self._wrap_(self)
        self.newItem = None

    def PreDeleteItem(self, flags, item):
        # Can detect cases where to stop via flags and condition below, however the operation
        # does not actual stop, we can resort to raising an exception as that does stop things
        # but that may need some additional considerations before implementing.
        return (
            0 if flags & shellcon.TSF_DELETE_RECYCLE_IF_POSSIBLE else 0x80004005
        )  # S_OK, or E_FAIL

    def PostDeleteItem(self, flags, item, hrDelete, newlyCreated):
        if newlyCreated:
            self.newItem = newlyCreated.GetDisplayName(shellcon.SHGDN_FORPARSING)

    def StartOperations(self):
        pass

    def FinishOperations(self, Result):
        pass

    def PreRenameItem(self, Flags, Item, NewName):
        pass

    def PostRenameItem(self, Flags, Item, NewName, hrRename, NewlyCreated):
        pass

    def PreMoveItem(self, Flags, Item, DestinationFolder, NewName):
        pass

    def PostMoveItem(
        self, Flags, Item, DestinationFolder, NewName, hrMove, NewlyCreated
    ):
        pass

    def PreCopyItem(self, Flags, Item, DestinationFolder, NewName):
        pass

    def PostCopyItem(
        self, Flags, Item, DestinationFolder, NewName, hrCopy, NewlyCreated
    ):
        pass

    def PreNewItem(self, Flags, DestinationFolder, NewName):
        pass

    def PostNewItem(
        self,
        Flags,
        DestinationFolder,
        NewName,
        TemplateName,
        FileAttributes,
        hrNew,
        NewItem,
    ):
        pass

    def UpdateProgress(self, WorkTotal, WorkSoFar):
        pass

    def ResetTimer(self):
        pass

    def PauseTimer(self):
        pass

    def ResumeTimer(self):
        pass


def CreateSink():
    return pythoncom.WrapObject(
        FileOperationProgressSink(), shell.IID_IFileOperationProgressSink
    )
