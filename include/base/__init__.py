from __future__ import absolute_import
from .. import mount

#: package name in which to include imported modules
IMPORT_PATH = mount.MOUNT_LOADER.name2mount(__name__)


def install():
    """Enable this type of include"""
    pass
