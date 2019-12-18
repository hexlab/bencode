# Bencode

Bencode is the encoding used by the p2p file sharing system BitTorrent.

## Example
```python
from bencode import bencode, bdecode
with open('1.torrent', 'rb') as binary_file:
    data = binary_file.read()
res = bdecode(data)
bytes_ = bencode(res)
```

## How to run tests

```python tests.py```

## Specs

#### Byte strings

Encoded as follows:

    <string length encoded in base ten ASCII>:<string data>

Examples:

    3:foo represents the string "foo"
    0: represents the empty string ""

#### Integers

Integers are encoded as follows: 

    i<integer encoded in base ten ASCII>e

Examples:

    i3e represents the integer "3"
    i-3e represents the integer "-3"
    i-0e is invalid. 
    i03e are invalid, but
    i0e represents the integer "0".

#### Lists

Lists are encoded as follows:

    l<bencoded values>e

The initial **l** and trailing **e** are beginning and ending delimiters. 
Lists may contain any bencoded type, including integers, strings, 
dictionaries, and even lists within other lists.

Represents

    l3:foo3:bare represents the list of two strings: ["foo", "bar"]
    le represents an empty list: []

#### Dictionaries

Dictionaries are encoded as follows: 

    d<bencoded string><bencoded element>e

The initial **d** and trailing **e** are the beginning and ending delimiters. 
Note that the keys must be bencoded strings. The values may be any
bencoded type, including integers, strings, lists, and other
dictionaries. Keys must be strings and appear in sorted order
(sorted as raw strings, not alphanumerics). The strings should be
compared using a binary comparison, not a culture-specific "natural"
comparison.

Examples:

    d4:dead4:beef3:foo3:bare represents the dictionary {"dead": "beef", "foo": "bar"}
    d3:fool1:a1:bee represents the dictionary {"foo": ["a", "b"]}
    d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee represents {"publisher": "bob", "publisher-webpage": "www.example.com", "publisher.location": "home"}
    de represents an empty dictionary {}
