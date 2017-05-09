from __future__ import absolute_import

INCLUDE_SCHEME = 'include.mount.files'


def install():
    import sys
    from . import import_hook
    from .. import _IMPORT_HOOKS
    if INCLUDE_SCHEME in _IMPORT_HOOKS:
        return
    hook = _IMPORT_HOOKS[INCLUDE_SCHEME] = import_hook.FilePathLoader(INCLUDE_SCHEME)
    sys.meta_path.append(hook)
