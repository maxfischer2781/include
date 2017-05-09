import sys


class MountLoader(object):
    def __init__(self, mount_prefix, module_prefix):
        self.prefix = mount_prefix
        self.module_prefix = module_prefix

    def load_module(self, name):
        """Load and return a module"""
        if name in sys.modules:
            return sys.modules[name]
        module_name = self.mount2name(name)
        __import__(module_name)
        module = sys.modules[name] = sys.modules[module_name]
        module.install()
        return module

    def find_module(self, name, path=None):
        if name.startswith(self.prefix):
            return self
        return None

    def name2mount(self, name):
        if not name.startswith(self.module_prefix):
            raise ValueError('Module name %r does not share prefix %r' % (name, self.module_prefix))
        return name.replace(self.module_prefix, self.prefix)

    def mount2name(self, mount):
        if not mount.startswith(self.prefix):
            raise ValueError('Module mount %r does not share prefix %r' % (mount, self.prefix))
        return mount.replace(self.prefix, self.module_prefix)


MOUNT_LOADER = MountLoader(mount_prefix=__package__, module_prefix=__package__.split('.', 1)[0])
sys.meta_path.append(MOUNT_LOADER)
