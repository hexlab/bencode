SEP, INT, DCT, LST, END = b':idle'
NUM = b'0123456789'


def decode(bstring: bytes, indx: int):
    byte = bstring[indx]
    if byte == INT:
        indx, end_indx = indx + 1, bstring.index(END, indx)
        return int(bstring[indx:end_indx]), end_indx + 1
    elif byte == LST:
        indx, lst = indx + 1, []
        while bstring[indx] != END:
            v, indx = decode(bstring, indx)
            lst.append(v)
        return lst, indx + 1
    elif byte == DCT:
        indx, dct = indx + 1, {}
        while bstring[indx] != END:
            key, indx = decode(bstring, indx)
            dct[key], indx = decode(bstring, indx)
        return dct, indx + 1
    else:
        sep_indx = bstring.index(SEP, indx)
        length = int(bstring[indx:sep_indx])
        sep_indx += 1
        return (bstring[sep_indx:sep_indx + length].decode('utf8'),
                sep_indx + length)


def bdecode(bstring):
    return decode(bstring, 0)[0]
