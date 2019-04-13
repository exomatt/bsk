from bitarray import bitarray

import spr2.readBinFile as readBinFile
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
    keys_list = keygenerator.generate_key(key)
    for i in range(16):
        temp_left = right_massage
        generate_key = keys_list[i]
        f_function_result = f_function(right_massage, generate_key)
        right_massage = left_message ^ f_function_result
        left_message = temp_left
    massage_after_iter = right_massage + left_message  # zamiana stron bo ostatni ma byc bez zamianay a petla domyslnie ostatenie tez zamieni miejscami x:D :P
    result_encryption = inverse_permutation(massage_after_iter)
    return result_encryption


# przyjmuje bit array i tu i tu czyli przed klucz słowny zamienic na bitarray
def decrypt_block(encrypted_message_in, key):
    permuted_message = init_permutation(encrypted_message_in)
    left_message, right_massage = spliHalf(permuted_message)

    keys_list = keygenerator.generate_key(key)[::-1]  # Reverse generated keys. [ 0, 1, 2... 15 ] -> [ 15, 14, 13... 0 ]

    for i in range(16):
        temp_left = right_massage
        generate_key = keys_list[i]
        f_function_result = f_function(right_massage, generate_key)
        right_massage = left_message ^ f_function_result
        left_message = temp_left

    massage_after_iter = right_massage + left_message  # zamiana stron bo ostatni ma byc bez zamianay a petla domyslnie ostatenie tez zamieni miejscami x:D :P
    result_decryption = inverse_permutation(massage_after_iter)
    return result_decryption


def encrypt_file_full_file(input_file, out, input_key):
    message_file = readBinFile.read_bin_file_to_bitarray(input_file)

    # add padding
    file_lenght = message_file.length() % 64
    if file_lenght != 0:
        to_add = 64 - file_lenght + 63
        message_file += bitarray("1")
        message_file += (to_add) * bitarray("0")
    else:
        message_file += bitarray("1")
        message_file += (63) * bitarray("0")

    encrypted_message = bitarray()
    for block in range(int(len(message_file) / 64)):
        block_message = message_file[(block * 64):((block + 1) * 64)]
        block_encrypted_message = encrypt_block(block_message, input_key)

        encrypted_message += block_encrypted_message

    readBinFile.write_bin_file(out, encrypted_message)


def decrypt_file_full_file(input_encrypted_file, out, input_key):
    message_encrypted_file = readBinFile.read_bin_file_to_bitarray(input_encrypted_file)

    decrypted_message = bitarray()
    for block in range(int(len(message_encrypted_file) / 64)):
        block_message = message_encrypted_file[(block * 64):((block + 1) * 64)]
        block_decrypted_message = decrypt_block(block_message, input_key)

        decrypted_message += block_decrypted_message

    # delete padding
    decrypted_message.reverse()
    message_copy = decrypted_message.copy()
    for num in range(len(decrypted_message)):
        if decrypted_message[num] == 1:
            message_copy.pop(0)
            break
        message_copy.pop(0)
    message_copy.reverse()
    readBinFile.write_bin_file(out, message_copy)


if __name__ == '__main__':
    # a = bitarray("1111111110100011101000111010001110100011101000111010001110100011")
    # barrayP = init_permutation(a)
    # print(barrayP)
    # left, right = spliHalf(barrayP)
    # print(left)
    # print(right)
    # permut = expand_with_E_permute(right)
    # print(permut)
    # print(a[:48])
    # print("wynik F funkcji ")
    # print(f_function(right, a[:48]))
    input_key = bitarray('1110011111000011111100001000011110100101110000111001011001101001')

    # 'smth.png' file size is 2112 bits, so -> (2112 % 64) == 0
    encrypt_file_full_file('smth.png', 'test1_encrypted.bin', input_key)  # encrypt file which (size % 64) == 0
    decrypt_file_full_file('test1_encrypted.bin', 'test1_decrypted.png',
                           input_key)  # decrypt file which (size % 64) == 0

    message = bitarray("1111111110100011101000111010001110100011101000111010001110100011")

    print('Message - ' + str(message))
    print(
        "INTERNET Encrypt:" + '110100010010010100111101000011010000111000010010001001011101110')  # Tak, nie ma początkowego zera

    encrypted = encrypt_block(message, input_key)
    print("Encrypted: " + str(encrypted))

    decrypted = decrypt_block(encrypted, input_key)
    print("Decrypted: " + str(decrypted))
