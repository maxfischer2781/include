from __future__ import absolute_import, division
import unittest
import tempfile
import textwrap
import pickle

import include


class TestHook(unittest.TestCase):
    def test_import_file(self):
        """compat: throw method"""
        container = tempfile.NamedTemporaryFile()
        shared_secret = 1337
        container.write(textwrap.dedent("""\
        class FileClass(object):
            shared_secret = %s
        """ % shared_secret).encode('ASCII'))
        container.flush()
        module = include.include_file(container.name)
        self.assertEqual(module.FileClass.shared_secret, shared_secret)
        self._test_defined(module.FileClass)

    def _test_defined(self, obj):
        self.assertEqual(obj, pickle.loads(pickle.dumps(obj)))
