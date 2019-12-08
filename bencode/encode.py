def encoder(obj):
    otype = type(obj)
    if otype == str:
        yield b'%d:%b' % (len(obj), obj.encode('utf8'))
    elif otype == dict:
        yield b'd'
        for k in sorted(obj):
            yield b'%d:%b' % (len(k), k.encode('utf8'))
            yield from encoder(obj[k])
        yield b'e'
    elif otype == list:
        yield b'l'
        for i in obj:
            yield from encoder(i)
        yield b'e'
    elif otype == bytes:
        yield b'%d:%b' % (len(obj), obj)
    elif otype in (int, bool):
        yield b'i%de' % obj
    else:
        obj = str(obj).encode('utf8')
        yield b'%d:%b' % (len(obj), obj)


def bencode(obj) -> bytes:
    return b''.join(encoder(obj))
