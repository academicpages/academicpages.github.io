from ..version import check_version


def test_check_version():
    """Test the behaviour of check_versionself.

    This is mostly used to make sure the pandoc version is appropriate for the library.
    """

    assert check_version("1.19.2.4", "1.12.1")
    assert check_version("2.2.3.2", "1.12.1")
    assert check_version("1.19.2.4", "1.12.1", max_v="2.0")
    assert not check_version("2.2.3.2", "1.12.1", max_v="2.0")
