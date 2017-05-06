from __future__ import absolute_import, division
import unittest
import tempfile
import textwrap
import pickle

import include


class TestHook(unittest.TestCase):
    def test_import_file(self):
        """import file path as module"""
        container = tempfile.NamedTemporaryFile()
        shared_secret = 1337
        container.write(textwrap.dedent("""\
        class FileClass(object):
            shared_secret = %s
        """ % shared_secret).encode('ASCII'))
        container.flush()
        module = include.include_file(container.name)
        class_id = id(module.FileClass)
        for _ in range(3):
            self.assertEqual(class_id, id(module.FileClass))
            self.assertEqual(module.FileClass.shared_secret, shared_secret)
            self._test_defined(module.FileClass)
            module = include.include_file(container.name)

    def _test_defined(self, obj):
        self.assertEqual(obj, pickle.loads(pickle.dumps(obj)))
