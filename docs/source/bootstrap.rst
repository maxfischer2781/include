Automatic Bootstrapping
#######################

Modules imported by :py:mod:`include` have an automatic bootstrapping mechanism:
when imported in another process, the required import hook is automatically loaded.
This allows un/pickling and transferring objects, without explicitly preparing :py:mod:`include` in the receiver.
The only restriction is that :py:mod:`include` must be importable *before* any module code is run.

Disabling Bootstrap Hooks
=========================

At times, bootstrapping arbitrary include types is not desired.
For example, a public web service may desire to run existing, local configuration code files during startup only.
As a simple remedy, individual include types can be disabled.

To disable include types, both a code and environment interface are available:

**Environment Variable** :py:envvar:`PY_INCLUDE_DISABLE`
    A list of include types to disable.
    Types are indicated by their module name, such as ``files`` for the ``include.files`` type.
    Multiple types may be delimited by commas, with optional whitespace.
    For example, the list ``files, encoded`` disables imports from files and encoded source.

**Code Interface** :py:func:`include.disable` and :py:func:`include.enable`
    Functions to disable or enable individual include types.
    Types may be indicated by a variety of identifiers.
    See :py:meth:`~.DisabledIncludeTypes.disable` for details.


Bootstrapping Mechanism
=======================

Each :py:mod:`include` corresponds to an include type *implementation* and *namespace*.
The former provides the actual import machinery, such as hooks and name translation.
The later is a namespace module, into which all modules imported by :py:mod:`include` are inserted.

For each include type, a separate namespace is used.
The namespace itself ensures that its include type is installed.
Thus, re-importing a module in a separate process first loads its namespace and thus its import machinery.

For example, a file based import is implemented in ``include.files``, and the default namespace is ``include.mount``.
When importing a file ``foo``, it is inserted as ``include.mount.files.foo``.
Re-importing ``include.mount.files.foo`` first imports ``include.mount.files``, which in turn installs ``include.files``.
