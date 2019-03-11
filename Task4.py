import string


def encrypt(word, key):
    alphabet = string.ascii_uppercase
    table = []
    for number in range(len(alphabet)):
        moved_alphabet = alphabet[number:] + alphabet[:number]
        table.append(moved_alphabet)
    encrypted = ''
    numberCol = 0
    for number in range(len(word)):
        row = ord(word[number]) - 65
        if numberCol >= len(key):
            numberCol = 0
        col = ord(key[numberCol]) - 65
        encrypted += table[col][row]
        numberCol += 1
    return encrypted


def decrypt(word, key):
    alphabet = string.ascii_uppercase
    table = []
    for number in range(len(alphabet)):
        moved_alphabet = alphabet[number:] + alphabet[:number]
        table.append(moved_alphabet)
    decrypted = ''
    numberCol = 0
    for number in range(len(word)):
        if numberCol >= len(key):
            numberCol = 0
        row = ord(key[numberCol]) - 65
        searched_letter = ord(word[number]) - 65
        row_alphabet = table[row]
        for element in range(len(row_alphabet)):
            if row_alphabet[element] == alphabet[searched_letter]:
                decrypted += alphabet[element]
                break
        numberCol += 1
    return decrypted


def __str__():
    return "Vigenere’a"


def main():
    # print(encrypt('CRYPTOGRAPHY', 'BREAKBREAKBR'))
    # print(decrypt('DICPDPXVAZIP', 'BREAKBREAKBR'))
    key = "BREAKBREAKBR"
    word = "CRYPTOGRAPHY"
    print(encrypt(word, key))
    pasw = decrypt(encrypt(word, key), key)
    print(pasw)
    print(word == pasw)


if __name__ == '__main__':
    main()
