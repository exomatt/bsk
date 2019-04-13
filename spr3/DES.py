from spr3.OwnBitarray import OwnBitarray
from bitarray import bitarray
import spr3.des_key as des_key


def generate_key(some_input):
    permuted_key = OwnBitarray()
    key_list_return = []

    for i in range(len(des_key.PC1)):
        permuted_key.append(some_input[des_key.PC1[i] - 1])

    L_K = permuted_key[0:28]
    R_K = permuted_key[28:56]

    for cycle_num in range(16):

        L_K = (L_K << des_key.SHIFT[cycle_num])  # Key shifting depends on number of cycle
        R_K = (R_K << des_key.SHIFT[cycle_num])  # Key shifting depends on number of cycle

        LR = OwnBitarray(L_K.to01() + R_K.to01())

        final_key = OwnBitarray()
        for i in range(len(des_key.PC2)):
            final_key.append(LR[des_key.PC2[i] - 1])
        key_list_return.append(final_key)

    return key_list_return


word = bitarray('0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111'.replace(' ', ''))

permuted_IP = bitarray()
for i in range(len(des_key.IP)):
    permuted_IP.append(word[des_key.IP[i] - 1])  # Liczę od 0,

L = permuted_IP[0:32]
R = permuted_IP[32:64]

# ---------------------------------------- GENERATE KEY ------------------------------------------

input_key = bitarray('00010011 00110100 01010111 01111001 10011011 10111100 11011111 11110001 '.replace(' ', ''))

key_list = []
key_list = generate_key(input_key)
