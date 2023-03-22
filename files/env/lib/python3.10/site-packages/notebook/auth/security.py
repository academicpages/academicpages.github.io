"""
Password generation for the Notebook.
"""

from contextlib import contextmanager
import getpass
import hashlib
import json
import os
import random
import traceback
import warnings

from ipython_genutils.py3compat import cast_bytes, str_to_bytes, cast_unicode
from traitlets.config import Config, ConfigFileNotFound, JSONFileConfigLoader
from jupyter_core.paths import jupyter_config_dir

# Length of the salt in nr of hex chars, which implies salt_len * 4
# bits of randomness.
salt_len = 12


def passwd(passphrase=None, algorithm='argon2'):
    """Generate hashed password and salt for use in notebook configuration.

    In the notebook configuration, set `c.NotebookApp.password` to
    the generated string.

    Parameters
    ----------
    passphrase : str
        Password to hash.  If unspecified, the user is asked to input
        and verify a password.
    algorithm : str
        Hashing algorithm to use (e.g, 'sha1' or any argument supported
        by :func:`hashlib.new`, or 'argon2').

    Returns
    -------
    hashed_passphrase : str
        Hashed password, in the format 'hash_algorithm:salt:passphrase_hash'.

    Examples
    --------
    >>> passwd('mypassword', algorithm='sha1')
    'sha1:7cf3:b7d6da294ea9592a9480c8f52e63cd42cfb9dd12'

    """
    if passphrase is None:
        for i in range(3):
            p0 = getpass.getpass('Enter password: ')
            p1 = getpass.getpass('Verify password: ')
            if p0 == p1:
                passphrase = p0
                break
            else:
                print('Passwords do not match.')
        else:
            raise ValueError('No matching passwords found. Giving up.')

    if algorithm == 'argon2':
        from argon2 import PasswordHasher
        ph = PasswordHasher(
            memory_cost=10240,
            time_cost=10,
            parallelism=8,
        )
        h = ph.hash(passphrase)

        return ':'.join((algorithm, cast_unicode(h, 'ascii')))
    else:
        h = hashlib.new(algorithm)
        salt = f"{random.getrandbits(4 * salt_len):0{salt_len}x}"
        h.update(cast_bytes(passphrase, 'utf-8') + str_to_bytes(salt, 'ascii'))

        return ':'.join((algorithm, salt, h.hexdigest()))


def passwd_check(hashed_passphrase, passphrase):
    """Verify that a given passphrase matches its hashed version.

    Parameters
    ----------
    hashed_passphrase : str
        Hashed password, in the format returned by `passwd`.
    passphrase : str
        Passphrase to validate.

    Returns
    -------
    valid : bool
        True if the passphrase matches the hash.

    Examples
    --------
    >>> from notebook.auth.security import passwd_check
    >>> passwd_check('argon2:...', 'mypassword')
    True

    >>> passwd_check('argon2:...', 'otherpassword')
    False

    >>> passwd_check('sha1:0e112c3ddfce:a68df677475c2b47b6e86d0467eec97ac5f4b85a',
    ...              'mypassword')
    True
    """
    if hashed_passphrase.startswith('argon2:'):
        import argon2
        import argon2.exceptions
        ph = argon2.PasswordHasher()
        try:
            return ph.verify(hashed_passphrase[7:], passphrase)
        except argon2.exceptions.VerificationError:
            return False
    else:
        try:
            algorithm, salt, pw_digest = hashed_passphrase.split(':', 2)
        except (ValueError, TypeError):
            return False

        try:
            h = hashlib.new(algorithm)
        except ValueError:
            return False

        if len(pw_digest) == 0:
            return False

        h.update(cast_bytes(passphrase, 'utf-8') + cast_bytes(salt, 'ascii'))

        return h.hexdigest() == pw_digest

@contextmanager
def persist_config(config_file=None, mode=0o600):
    """Context manager that can be used to modify a config object

    On exit of the context manager, the config will be written back to disk,
    by default with user-only (600) permissions.
    """

    if config_file is None:
        config_file = os.path.join(jupyter_config_dir(), 'jupyter_notebook_config.json')

    os.makedirs(os.path.dirname(config_file), exist_ok=True)

    loader = JSONFileConfigLoader(os.path.basename(config_file), os.path.dirname(config_file))
    try:
        config = loader.load_config()
    except ConfigFileNotFound:
        config = Config()

    yield config

    with open(config_file, 'w', encoding='utf8') as f:
        f.write(cast_unicode(json.dumps(config, indent=2)))

    try:
        os.chmod(config_file, mode)
    except Exception as e:
        tb = traceback.format_exc()
        warnings.warn(f"Failed to set permissions on {config_file}:\n{tb}",
            RuntimeWarning)


def set_password(password=None, config_file=None):
    """Ask user for password, store it in notebook json configuration file"""

    hashed_password = passwd(password)

    with persist_config(config_file) as config:
        config.NotebookApp.password = hashed_password
