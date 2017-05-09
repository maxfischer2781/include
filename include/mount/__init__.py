import sys


class MetaLoader(object):
    def __init__(self, mount_prefix, module_prefix):
        self.prefix = mount_prefix
        self.module_prefix = module_prefix

    def load_module(self, name):
        """Load and return a module"""
        if name in sys.modules:
            return sys.modules[name]
        module_name = name.replace(self.prefix, self.module_prefix)
        __import__(module_name)
        module = sys.modules[name] = sys.modules[module_name]
        module.install()
        return module

    def find_module(self, name, path=None):
        if name.startswith(self.prefix):
            return self
        return None


sys.meta_path.append(MetaLoader(mount_prefix=__package__, module_prefix=__package__.split('.', 1)[0]))
