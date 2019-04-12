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


if __name__ == '__main__':
    a = bitarray("1111111110100011101000111010001110100011101000111010001110100011")
    barrayP = init_permutation(a)
    print(barrayP)
    left, right = spliHalf(barrayP)
    print(left)
    print(right)
    print(expand_with_E_permut(right))
