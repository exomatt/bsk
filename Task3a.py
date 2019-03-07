# Caesar cipher


def encrypt(word, move):
    move = int(move)
    word = word.upper()
    encrypted = ''
    for letter in word:
        letter_after_move = ord(letter) + move
        if letter_after_move > ord('Z'):
            letter_after_move = letter_after_move - 26
        encrypted += chr(letter_after_move)

    return encrypted


def decrypt(word, move):
    move = int(move)
    word = word.upper()
    decrypted = ''
    for letter in word:
        letter_after_move = ord(letter) - move
        if letter_after_move < ord('A'):
            letter_after_move = letter_after_move + 26
        if letter_after_move > ord('Z'):
            letter_after_move = letter_after_move - 26
        decrypted += chr(letter_after_move)

    return decrypted


def __str__():
    return "Ceasar"

# def main():
#     print(encrypt('CRYPTOGRAPHY', 3))
#     print(decrypt('FUBSWRJUDSKB', 3))
#
#
# if __name__ == '__main__':
#     main()
