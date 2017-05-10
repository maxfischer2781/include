from __future__ import absolute_import, division
import unittest
import tempfile
import textwrap
import pickle
import multiprocessing

import include


class TestHook(unittest.TestCase):
    def test_import_file(self):
        """import file path as module"""
        container = tempfile.NamedTemporaryFile()
        shared_secret = 1337
        container.write(textwrap.dedent("""\
        class FileClass(object):
            shared_secret = %s

            def __init__(self, value):
                self.value = value

            def __eq__(self, other):
                return self.value == other.value
        """ % shared_secret).encode('ASCII'))
        container.flush()
        module = include.path(container.name)
        class_id = id(module.FileClass)
        for _ in range(3):
            self.assertEqual(class_id, id(module.FileClass))
            self.assertEqual(module.FileClass.shared_secret, shared_secret)
            self._test_defined(module.FileClass, ('shared_secret', ))
            self._test_defined(module.FileClass(5), ('shared_secret', 'value'))
            module = include.path(container.name)

    def _test_defined(self, obj, attr_names=()):
        self.assertEqual(obj, pickle.loads(pickle.dumps(obj)))
        for name in attr_names:
            self.assertEqual(getattr(obj, name), getattr(pickle.loads(pickle.dumps(obj)), name))
        # test in separate process
        pool = multiprocessing.Pool(1)
        for name in attr_names:
            self.assertEqual(getattr(obj, name), pool.apply(getattr, (obj, name)))
        pool.close()
