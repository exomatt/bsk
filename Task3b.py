import string
from math import gcd


def coprime(a, b):
    return gcd(a, b) == 1


def encrypt(word, n, k1, k0):
    if coprime(k1, n) and coprime(k0, n):
        encrypted = ''
        alphabet = string.ascii_uppercase
        for letter in word:
            encrypted_letter = ((ord(letter) - 65) * k1 + k0) % n
            encrypted += alphabet[encrypted_letter]
        return encrypted
    else:
        return 'Error'


def decrypt(word, n, k1, k0, fn):
    if coprime(k1, n) and coprime(k0, n):
        decrypted = ''
        alphabet = string.ascii_uppercase
        for letter in word:
            decrypted_letter = (((ord(letter) - 65) + (n - k0))*(k1 ** (fn - 1))) % n
            decrypted += alphabet[decrypted_letter]
        return decrypted
    else:
        return 'Error'


def main():
    print(encrypt('CRYPTOGRAPHY', 21, 5, 4))
    print(decrypt('OFTQPLNFEQST', 21, 5, 4, 12))
    print(encrypt('CRYPTOGRAPHY', 26, 7, 5))
    print(decrypt('TURGIZVUFGCR', 26, 7, 5, 12))


if __name__ == '__main__':
    main()
