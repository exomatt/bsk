from bitarray import bitarray

import string
import spr3.des_key as des_key

def generate_key(input, num_of_cycle):
    permuted_key = bitarray()

    for i in range(len(des_key.PC1)):
        permuted_key.append(input[des_key.PC1[i]-1])

    L_K = permuted_key[0:28]
    R_K = permuted_key[28:56]


    return permuted_key

word = bitarray(('0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111').replace(' ',''))
#print(str(word) + ' word')
permuted_IP = bitarray()
for i in range(len(des_key.IP)):
    permuted_IP.append(word[des_key.IP[i]-1]) #Liczę od 0,

#print(str(permuted_IP) + ' - permuted_IP')

L = permuted_IP[0:32]
R = permuted_IP[32:64]
#print(str(L) + ' L - of permuted_IP')
#print(str(R) + ' R - of permuted_IP')

#---------------------------------------- GENERATE KEY ------------------------------------------

input_key = bitarray(('1110 0111 1100 0011 1111 0000 1000 0111 1010 0101 1100 0011 1001 0110 0110 1001').replace(' ',''))

key = generate_key(input_key)
