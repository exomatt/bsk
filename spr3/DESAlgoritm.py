from bitarray import bitarray

import spr3.des_key as des_key


# za parametr przyjmuje bitarray :)

def init_permutation(barray):
    array_after_permut = bitarray()
    for number in range(len(des_key.IP)):
        array_after_permut.append(barray[des_key.IP[number] - 1])
    return array_after_permut


def spliHalf(barray):
    return barray[:32], barray[32:]


def expand_with_E_permut(barray):
    array_after_expand = bitarray()
    for number in range(len(des_key.E)):
        array_after_expand.append(barray[des_key.E[number] - 1])
    return array_after_expand


def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i + n]


def f_function(barray, key):
    own_bitarray = bitarray(barray ^ key)
    bit_arrays = list(chunks(own_bitarray, 6))
    number = 0
    temp_to_add = ''
    for arr in bit_arrays:
        f_l_elements = arr[::5]
        mid_elements = arr[1:5]
        first = int(f_l_elements.to01(), 2)
        second = int(mid_elements.to01(), 2)
        s_box = des_key.S_BOX
        temp_to_add += str(bin(s_box[number][first][second]))[2:].zfill(4)
        number += 1
    return bitarray(temp_to_add)


if __name__ == '__main__':
    a = bitarray("1111111110100011101000111010001110100011101000111010001110100011")

    barrayP = init_permutation(a)
    print(barrayP)
    left, right = spliHalf(barrayP)
    print(left)
    print(right)
    permut = expand_with_E_permut(right)
    print(permut)
    print(a[:48])
    print(f_function(permut, a[:48]))
