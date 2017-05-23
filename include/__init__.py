from __future__ import absolute_import
import sys
import weakref

# weak reference to installed hooks
_IMPORT_HOOKS = weakref.WeakValueDictionary()


def path(file_path):
    """
    Include module code from a file identified by its path

    :param file_path: path to a file containing module code
    :type file_path: str
    :return: the imported module
    :rtype: module

    Comparable to ``execfile``, but respects the rules and constraints of modules.
    If invoked again with the same ``file_path``, the same module is returned.
    """
    from . import files
    return _import_url(module_url=file_path, include_type=files)


def source(source_code):
    """
    Include module code directly from a string

    :param source_code: source code of the module
    :type source_code: str
    :return: the imported module
    :rtype: module

    Comparable to ``exec`` in a separate ``globals`` namespace, but respects the rules and constraints of modules.
    If invoked again with the same ``source_code``, the same module is returned.
    """
    from . import encoded
    return _import_url(module_url=source_code, include_type=encoded)


def _import_url(module_url, include_type):
    if include_type.IMPORT_PATH not in _IMPORT_HOOKS:
        include_type.install()
    import_hook = _IMPORT_HOOKS[include_type.IMPORT_PATH]
    module_path = import_hook.uri2module(module_url)
    __import__(module_path)
    return sys.modules[module_path]
