from __future__ import absolute_import
from .. import mount

INCLUDE_SCHEME = mount.MOUNT_LOADER.name2mount(__name__)


def install():
    import sys
    from . import import_hook
    from .. import _IMPORT_HOOKS
    if INCLUDE_SCHEME in _IMPORT_HOOKS:
        return
    hook = _IMPORT_HOOKS[INCLUDE_SCHEME] = import_hook.FilePathLoader(INCLUDE_SCHEME)
    sys.meta_path.insert(sys.meta_path.index(mount.MOUNT_LOADER), hook)
