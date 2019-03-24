import bitarray


# return bitarray.bitarray
def read_bin_file_to_bitarray(name):
    a = bitarray.bitarray()
    with open(name, 'rb') as fh:
        a.fromfile(fh)
    return a


# return string with  0 1 only
def read_bin_file_to_bitarray_string(name):
    a = bitarray.bitarray()
    with open(name, 'rb') as fh:
        a.fromfile(fh)
    return a.to01()


# write  bitarray.bitarray
def write_bin_file(name, array):
    with open(name, 'wb') as fh:
        array.tofile(fh)


# write  string with  0 1 only
def write_bin_file_string(name, string):
    a = bitarray.bitarray()
    a.fromstring(string)
    with open(name, 'wb') as fh:
        a.tofile(fh)


def main():
    test__bin = '/home/exomat/Pulpit/bsk/spr2/test3.bin'
    bitarray = read_bin_file_to_bitarray(test__bin)
    print(bitarray)
    write_bin_file_string('testwrite2.bin', bitarray.to01())


if __name__ == '__main__':
    main()
