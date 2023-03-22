import json
import os
import shutil
import tempfile

from notebook.config_manager import BaseJSONConfigManager


def test_json():
    tmpdir = tempfile.mkdtemp()
    try:
        root_data = dict(a=1, x=2, nest={'a':1, 'x':2})
        with open(os.path.join(tmpdir, 'foo.json'), 'w') as f:
            json.dump(root_data, f)
        # also make a foo.d/ directory with multiple json files
        os.makedirs(os.path.join(tmpdir, 'foo.d'))
        with open(os.path.join(tmpdir, 'foo.d', 'a.json'), 'w') as f:
            json.dump(dict(a=2, b=1, nest={'a':2, 'b':1}), f)
        with open(os.path.join(tmpdir, 'foo.d', 'b.json'), 'w') as f:
            json.dump(dict(a=3, b=2, c=3, nest={'a':3, 'b':2, 'c':3}, only_in_b={'x':1}), f)
        manager = BaseJSONConfigManager(config_dir=tmpdir, read_directory=False)
        data = manager.get('foo')
        assert 'a' in data
        assert 'x' in data
        assert 'b' not in data
        assert 'c' not in data
        assert data['a'] == 1
        assert 'x' in data['nest']
        # if we write it out, it also shouldn't pick up the subdirectory
        manager.set('foo', data)
        data = manager.get('foo')
        assert data == root_data

        manager = BaseJSONConfigManager(config_dir=tmpdir, read_directory=True)
        data = manager.get('foo')
        assert 'a' in data
        assert 'b' in data
        assert 'c' in data
        # files should be read in order foo.d/a.json foo.d/b.json foo.json
        assert data['a'] == 1
        assert data['b'] == 2
        assert data['c'] == 3
        assert data['nest']['a'] == 1
        assert data['nest']['b'] == 2
        assert data['nest']['c'] == 3
        assert data['nest']['x'] == 2

        # when writing out, we don't want foo.d/*.json data to be included in the root foo.json
        manager.set('foo', data)
        manager = BaseJSONConfigManager(config_dir=tmpdir, read_directory=False)
        data = manager.get('foo')
        assert data == root_data

    finally:
        shutil.rmtree(tmpdir)


