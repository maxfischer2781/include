from __future__ import absolute_import
import sys
import weakref

# weak reference to installed hooks
_IMPORT_HOOKS = weakref.WeakValueDictionary()


def include_file(path):
    if 'file' not in _IMPORT_HOOKS:
        from . import files
        files.install()
    import_hook = _IMPORT_HOOKS['file']
    module_path = import_hook.path2module(path)
    __import__(module_path)
    return sys.modules[module_path]
