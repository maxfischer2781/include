#################################
include - Dynamic Module Importer
#################################

When you just need that code, ``include`` does the ugly bits for you.
It allows you to run code from files, strings or other sources as if they were regular modules.
Code is executed as compliant as possible with the Python ecosystem.
The resulting modules and objects can be pickled, copied and sent to other processes.
This makes ``include`` suitable for testing, configuration, code creation and more.

Usage
#####

``include`` provides a simple API that works similar to the ``__import__`` builtin.
To import a module from its file path, pass it to the ``include.path`` function:

.. code:: python

    import include
    conf_module = include.path('/etc/myapp/conf.py')

Once a module has been imported by ``include``, it does not require special handling.
You can work with the resulting module and its content without using ``include`` explicitly.

:note: The ``include`` package must be importable by any python process working with a module imported by ``include``.
