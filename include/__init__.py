from __future__ import absolute_import
import sys

IMPORT_HOOKS = {}


def include_file(path):
    if 'file' not in IMPORT_HOOKS:
        from . import files
        files.install()
    import_hook = IMPORT_HOOKS['file']
    module_path = import_hook.path2module(path)
    __import__(module_path)
    return sys.modules[module_path]
