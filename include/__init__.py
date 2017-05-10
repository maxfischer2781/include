from __future__ import absolute_import
import sys
import weakref

# weak reference to installed hooks
_IMPORT_HOOKS = weakref.WeakValueDictionary()


def path(file_path):
    from . import files
    if files.IMPORT_PATH not in _IMPORT_HOOKS:
        files.install()
    import_hook = _IMPORT_HOOKS[files.IMPORT_PATH]
    module_path = import_hook.path2module(file_path)
    __import__(module_path)
    return sys.modules[module_path]
