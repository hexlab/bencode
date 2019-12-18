import unittest

from bencode import bencode


class TestEncoder(unittest.TestCase):

    def test_encode_str(self):
        self.assertEqual(bencode(''), b'0:')
        self.assertEqual(bencode('foo'), b'3:foo')
