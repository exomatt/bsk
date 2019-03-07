import math
import string
from math import gcd


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount


def coprime(a, b):
    return gcd(a, b) == 1


def encrypt(word, n, k1, k0):
    n = int(n)
    k1 = int(k1)
    k0 = int(k0)
    if coprime(k1, n) and coprime(k0, n):
        encrypted = ''
        alphabet = string.ascii_uppercase
        for letter in word:
            encrypted_letter = ((ord(letter) - 65) * k1 + k0) % n
            encrypted += alphabet[encrypted_letter]
        return encrypted
    else:
        return 'Error'


def decrypt(word, n, k1, k0):
    n = int(n)
    k1 = int(k1)
    k0 = int(k0)
    if coprime(k1, n) and coprime(k0, n):
        decrypted = ''
        alphabet = string.ascii_uppercase
        for letter in word:
            decrypted_letter = (((ord(letter) - 65) + (n - k0)) * (k1 ** (phi(n) - 1))) % n
            decrypted += alphabet[decrypted_letter]
        return decrypted
    else:
        return 'Error'


def __str__():
    return "Ceasar B"


def main():
    print(encrypt('CRYPTOGRAPHY', 26, 7, 5))
    print(decrypt('TURGIZVUFGCR', 26, 7, 5))


if __name__ == '__main__':
    main()
