from __future__ import absolute_import
import sys
import weakref

# weak reference to installed hooks
_IMPORT_HOOKS = weakref.WeakValueDictionary()


def include_file(path):
    from . import files
    if files.INCLUDE_SCHEME not in _IMPORT_HOOKS:
        files.install()
    import_hook = _IMPORT_HOOKS[files.INCLUDE_SCHEME]
    module_path = import_hook.path2module(path)
    __import__(module_path)
    return sys.modules[module_path]
