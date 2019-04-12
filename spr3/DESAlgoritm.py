from bitarray import bitarray

import spr3.DES as keygenerator
import spr3.des_key as des_key


# za parametr przyjmuje bitarray :)

def init_permutation(bit_array):
    array_after_permut = bitarray()
    for number in range(len(des_key.IP)):
        array_after_permut.append(bit_array[des_key.IP[number] - 1])
    return array_after_permut


def inverse_permutation(bit_array):
    array_after_permut = bitarray()
    for number in range(len(des_key.IPR)):
        array_after_permut.append(bit_array[des_key.IPR[number] - 1])
    return array_after_permut


def spliHalf(barray):
    return barray[:32], barray[32:]


def expand_with_E_permute(bit_array):
    array_after_expand = bitarray()
    for number in range(len(des_key.E)):
        array_after_expand.append(bit_array[des_key.E[number] - 1])
    return array_after_expand


def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i + n]


def f_function(bit_array, key):
    e_permute = expand_with_E_permute(bit_array)
    own_bit_array = bitarray(e_permute ^ key)
    bit_arrays = list(chunks(own_bit_array, 6))
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
    result_of_s_box_operant = bitarray(temp_to_add)
    array_after_permut = bitarray()
    for number in range(len(des_key.P)):
        array_after_permut.append(result_of_s_box_operant[des_key.P[number] - 1])
    return array_after_permut


# przyjmuje bit array i tu i tu czyli przed klucz słowny zamienic na bitarray
def encrypt_block(message_in, key):
    permuted_message = init_permutation(message_in)
    left_message, right_massage = spliHalf(permuted_message)
    for i in range(16):
        temp_left = right_massage
        generate_key = keygenerator.generate_key(key, i)
        f_function_result = f_function(right_massage, generate_key)
        right_massage = left_message ^ f_function_result
        left_message = temp_left
    massage_after_iter = right_massage + left_message  # zamiana stron bo ostatni ma byc bez zamianay a petla domyslnie ostatenie tez zamieni miejscami x:D :P
    result_encryption = inverse_permutation(massage_after_iter)
    return result_encryption


if __name__ == '__main__':
    a = bitarray("1111111110100011101000111010001110100011101000111010001110100011")
    barrayP = init_permutation(a)
    print(barrayP)
    left, right = spliHalf(barrayP)
    print(left)
    print(right)
    permut = expand_with_E_permute(right)
    print(permut)
    print(a[:48])
    print("wynik F funkcji ")
    print(f_function(right, a[:48]))
    input_key = bitarray('1110011111000011111100001000011110100101110000111001011001101001')
    message = bitarray("1111111110100011101000111010001110100011101000111010001110100011")
    print("Encrypted: ")
    print("right is 0001 0011 0010 0001 0010 0100 1011 0111")
    print(encrypt_block(message, input_key))
