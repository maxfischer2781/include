import os
import sys
import imp

from ..base import import_hook


class FilePathLoader(import_hook.BaseIncludeLoader):
    """
    Load python file from their path

    This import hook allows using encoded paths as module names to load modules
    directly from their file.
    """
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
            module = imp.load_source(name, path)
        module.__loader__ = self
        sys.modules[name] = module
        return module
