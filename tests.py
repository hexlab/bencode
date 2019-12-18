import unittest

from bencode import bencode, bdecode


TEST_CASES = (
    (b'0:', ''),
    (b'3:foo', 'foo'),
    (b'i3e', 3),
    (b'i-3e', -3),
    (b'i0e', 0),
    (b'le', []),
    (b'l3:foo3:bare', ["foo", "bar"]),
    (b'li1ee', [1]),
    (b'de', {}),
    (b'd4:dead4:beef3:foo3:bare', {"foo": "bar", "dead": "beef"}),
    (b'd3:fool1:a1:bee', {"foo": ["a", "b"]}),
    (b'd9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee',
     {"publisher": "bob", "publisher-webpage": "www.example.com", "publisher.location": "home"}),
)


class TestBencode(unittest.TestCase):

    def test_bencode(self):
        for encoded, obj in TEST_CASES:
            bencoded = bencode(obj)
            assert bencoded == encoded, \
                f'{obj} encoded as {bencoded} != {encoded}'

    def test_bdecode(self):
        for encoded, obj in TEST_CASES:
            bdecoded = bdecode(encoded)
            assert bdecoded == obj, \
                f'{encoded} decoded as {bdecoded} != "{obj}"'


if __name__ == '__main__':
    unittest.main()
