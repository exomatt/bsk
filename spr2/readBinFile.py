import bitarray


# return bitarray.bitarray
def read_bin_file_to_bitarray(name):
    a = bitarray.bitarray()
    with open(name, 'rb') as fh:
        a.fromfile(fh)
    return a


# return string with 0 1 only
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


def compare_two_bin_files(file1, file2):
    for i in file1:
        if file1[i] != file2[i]:
            return False
    return True


def main():
    test__bin = '/home/damian/Projects/BSK/spr2/test3.bin'
    array = read_bin_file_to_bitarray(test__bin)

    print(array)
    write_bin_file_string('zad3_input_X.bin', array.to01())
    return array


if __name__ == '__main__':
    main()
