from nbconvert.filters import get_metadata


def test_get_metadata():
    output = {
        "metadata": {
            "width": 1,
            "height": 2,
            "image/png": {
                "unconfined": True,
                "height": 3,
            },
        }
    }
    assert get_metadata(output, "nowhere") is None
    assert get_metadata(output, "height") == 2
    assert get_metadata(output, "unconfined") is None
    assert get_metadata(output, "unconfined", "image/png") is True
    assert get_metadata(output, "width", "image/png") == 1
    assert get_metadata(output, "height", "image/png") == 3
