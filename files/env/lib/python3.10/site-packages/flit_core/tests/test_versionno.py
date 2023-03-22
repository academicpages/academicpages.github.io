import pytest

from flit_core.common import InvalidVersion
from flit_core.versionno import normalise_version

def test_normalise_version():
    nv = normalise_version
    assert nv('4.3.1') == '4.3.1'
    assert nv('1.0b2') == '1.0b2'
    assert nv('2!1.3') == '2!1.3'

    # Prereleases
    assert nv('1.0B2') == '1.0b2'
    assert nv('1.0.b2') == '1.0b2'
    assert nv('1.0beta2') == '1.0b2'
    assert nv('1.01beta002') == '1.1b2'
    assert nv('1.0-preview2') == '1.0rc2'
    assert nv('1.0_c') == '1.0rc0'

    # Post releases
    assert nv('1.0post-2') == '1.0.post2'
    assert nv('1.0post') == '1.0.post0'
    assert nv('1.0-rev3') == '1.0.post3'
    assert nv('1.0-2') == '1.0.post2'

    # Development versions
    assert nv('1.0dev-2') == '1.0.dev2'
    assert nv('1.0dev') == '1.0.dev0'
    assert nv('1.0-dev3') == '1.0.dev3'

    assert nv('1.0+ubuntu-01') == '1.0+ubuntu.1'
    assert nv('v1.3-pre2') == '1.3rc2'
    assert nv(' 1.2.5.6\t') == '1.2.5.6'
    assert nv('1.0-alpha3-post02+ubuntu_xenial_5') == '1.0a3.post2+ubuntu.xenial.5'

    with pytest.raises(InvalidVersion):
        nv('3!')

    with pytest.raises(InvalidVersion):
        nv('abc')
