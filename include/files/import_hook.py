import os
import sys
import imp

from ..base import import_hook


class FilePathLoader(import_hook.BaseIncludeLoader):
    """
    Load python file from their path

    This import hook allows using encoded paths as module names to load modules
    directly from their file.  File path modules use a special naming convention as
    ``<module_prefix>.<escaped path>``, where ``escaped path`` is stripped of any
    import specific symbols (``.`` and ``/``).

    :param module_prefix: prefix for modules to import
    :type module_prefix: str

    The ``module_prefix`` is used to distinguish regular and file based imports.
    It may be any valid module or package name, including dots. Logically, all
    imported files will be submodules of the package pointed to by ``module_prefix``.

    Note that ``module_prefix`` must point to a valid package, not a module.
    """
    def module2uri(self, module_name):
        """Convert a module name to a path"""
        assert module_name.startswith(self.prefix), 'incompatible module name'
        path = module_name[len(self._prefix):]
        path = path.replace('&#DOT', '.')
        return path.replace('&#SEP', os.sep)

    def uri2module(self, path):
        """Convert a path to a module name"""
        module_name = path.replace('.', '&#DOT')
        module_name = module_name.replace(os.sep, '&#SEP')
        return self.prefix + module_name

    def load_module(self, name):
        """
        Load and return a module

        Always returns the corresponding module. If the module is already
        loaded, the existing module is returned.
        """
        if name in sys.modules:
            return sys.modules[name]
        path = self.module2uri(name)
        if not os.path.isfile(path):
            raise ImportError("Missing module source file %r" % path)
        else:
            with open(path) as module_source:
                module = imp.load_module(name, module_source, path, ('.py', 'U', imp.PY_SOURCE))
        sys.modules[name] = module
        return module
