from __future__ import absolute_import


def install():
    import sys
    from . import import_hook
    import include
    if 'file' in include.IMPORT_HOOKS:
        return
    include.IMPORT_HOOKS['file'] = import_hook.FilePathLoader('file')
    sys.meta_path.append(include.IMPORT_HOOKS['file'])
