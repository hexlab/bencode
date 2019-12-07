SEP, INT, DCT, LST, END = b':idle'
NUM = b'0123456789'


def parse_int(bstring: bytes, indx: int) -> (int, int):
    indx, end_indx = indx + 1, bstring.index(END, indx)
    return int(bstring[indx:end_indx]), end_indx + 1


def parse_string(bstring: bytes, indx: int) -> (bytes, int):
    sep_indx = bstring.index(SEP, indx)
    length = int(bstring[indx:sep_indx])
    sep_indx += 1
    return bstring[sep_indx:sep_indx + length], sep_indx + length


def parse_list(bstring: bytes, indx: int) -> (list, int):
    indx, lst = indx + 1, []
    while bstring[indx] != END:
        v, indx = parsers[bstring[indx]](bstring, indx)
        lst.append(v)
    return lst, indx + 1


def parse_dict(bstring: bytes, indx: int) -> (dict, int):
    indx, dct = indx + 1, {}
    while bstring[indx] != END:
        key, indx = parse_string(bstring, indx)
        dct[key], indx = parsers[bstring[indx]](bstring, indx)
    return dct, indx + 1


parsers = {i: parse_string for i in NUM}
parsers[LST] = parse_list
parsers[DCT] = parse_dict
parsers[INT] = parse_int


def bdecode(bstring: bytes):
    return parsers[bstring[0]](bstring, 0)[0]
