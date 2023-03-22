version_info = (6, 5, 4)
pre_info = ""
dev_info = ""


def create_valid_version(release_info, epoch=None, pre_input="", dev_input=""):
    """
    Creates a pep440 valid version of version number given a tuple integers
    and optional epoch, prerelease and developmental info.

    Parameters
    ----------
    release_info : Tuple(Int)
    epoch : Int, default None
    pre_input : Str, default ''
    dev_input : Str, default ''
    """

    pep440_err = "The version number is not a pep 440 compliant version number"

    if epoch is not None:
        epoch_seg = str(epoch) + "!"
    else:
        epoch_seg = ""

    release_seg = ".".join(map(str, release_info))

    _magic_pre = ["a", "b", "rc"]
    if pre_input != "" and not any([pre_input.startswith(prefix) for prefix in _magic_pre]):
        raise ValueError(pep440_err + "\n please fix your prerelease segment.")
    else:
        pre_seg = pre_input

    if dev_input == "":
        dev_seg = dev_input
    elif not dev_input.startswith(".") and dev_input.startswith("dev"):
        dev_seg = "".join([".", dev_input])
    elif dev_input.startswith(".dev"):
        dev_seg = dev_input
    elif dev_input != "":
        raise ValueError(pep440_err + "\n please fix your development segment.")

    if dev_input != "" and not any([dev_seg.endswith(str(n)) for n in range(10)]):
        dev_seg = "".join([dev_seg, "0"])

    out_version = "".join([epoch_seg, release_seg, pre_seg, dev_seg])

    import re

    def is_canonical(version):
        return (
            re.match(
                r"^([1-9]\d*!)?(0|[1-9]\d*)"
                r"(\.(0|[1-9]\d*))*((a|b|rc)(0|[1-9]\d*))?"
                r"(\.post(0|[1-9]\d*))?(\.dev(0|[1-9]\d*))?$",
                version,
            )
            is not None
        )

    if is_canonical(out_version):
        return out_version
    else:
        raise ValueError(pep440_err)


__version__ = create_valid_version(version_info, pre_input=pre_info, dev_input=dev_info)
