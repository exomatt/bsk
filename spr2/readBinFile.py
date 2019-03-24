import bitarray


def read_bin_file_to_bitarray(name):
    a = bitarray.bitarray()
    with open(name, 'rb') as fh:
        a.fromfile(fh)
    return a


def write_bin_file(name, array):
    with open(name, 'wb') as fh:
        array.tofile(fh)


def main():
    test__bin = '/home/exomat/Pulpit/bsk/spr2/test3.bin'
    bitarray = read_bin_file_to_bitarray(test__bin)
    print(bitarray)
    write_bin_file('testwrite.bin',bitarray)

if __name__ == '__main__':
    main()
