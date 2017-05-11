import os


class BaseIncludeLoader(object):
    """
    Import hook to load Python modules from an arbitrary location

    :param module_prefix: prefix for modules to import
    :type module_prefix: str

    Base class for import hooks to non-standard code sources. Implements the
    general structure for encoded sources: a module source translates to an
    artificial module path of the form ``<module_prefix>.<encoded_name>``. The
    ``module_prefix`` identifies the code source type (and import hook) while the
    ``encoded_name`` contains all required information to retrieve the code.

    For example, a ``module_prefix`` of ``include.type.files`` could identify
    a source file type, and an ``encoded_name`` of ``SLASHtmpSLASHfooDOTpy`` point
    to the path ``/tmp/foo.py``. The resulting module would appear as
    ``include.type.files.SLASHtmpSLASHfooDOTpy``.

    Note that ``module_prefix`` must point to a valid package, not a module.
    It will be actually imported by the regular import machinery, and can be
    used to bootstrap hooks.

    The ``encoded_name`` is a free form field. The base class provides means to
    escape invalid and reserved symbols (``/`` and ``.``), but subclasses are
    free to use them if it is suitable for them. Hooks should use ``encoded_name``
    to store a URI (or similar) to retrieve source code. As per Python rules,
    including a dot (``.``) in the ``encoded_name`` requires the hook to import
    each portion separately.
    """
    def __init__(self, module_prefix):
        self._prefix = ''
        self.prefix = module_prefix

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        self._prefix = value + '.'

    def module2uri(self, module_name):
        """Convert an unencoded source uri to an encoded module name"""
        assert module_name.startswith(self.prefix), 'incompatible module name'
        path = module_name[len(self._prefix):]
        path = path.replace('&#DOT', '.')
        return path.replace('&#SEP', os.sep)

    def uri2module(self, uri):
        """Convert an encoded module name to an unencoded source uri"""
        module_name = uri.replace('.', '&#DOT')
        module_name = module_name.replace(os.sep, '&#SEP')
        return self.prefix + module_name

    def load_module(self, name):
        """
        Load and return a module

        Always returns the corresponding module. If the module is already
        loaded, the existing module is returned.
        """
        raise NotImplementedError

    def find_module(self, name, path=None):
        if name.startswith(self.prefix):
            return self
        else:
            return None
