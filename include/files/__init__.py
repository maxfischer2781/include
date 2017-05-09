from __future__ import absolute_import


def install():
    import sys
    from . import import_hook
    from .. import _IMPORT_HOOKS
    if 'file' in _IMPORT_HOOKS:
        return
    hook = _IMPORT_HOOKS['file'] = import_hook.FilePathLoader('file')
    sys.meta_path.append(hook)
