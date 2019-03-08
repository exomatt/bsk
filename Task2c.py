import string
import copy


def p(item):
    print("-----")
    print(item)
    print("-----")


def encrypt(word, key):
    alphabet = string.ascii_uppercase
    order = []
    number = 0
    for i in range(len(key)):
        order.append("")
    for char in alphabet:
        for letter_number in range(len(key)):
            if char == key[letter_number]:
                order[letter_number] = number
                number += 1
    table = [""] * len(key)
    for row in range(len(table)):
        table[row] = [""] * len(key)

    for row in range(len(table)):
        for col in range(len(table[row])):
            if col <= order[row]:
                table[row][col] = "\u0000"
    number_of_tables = int(len(word) / (((1 + len(key)) * len(key)) / 2))
    if len(word) % (((1 + len(key)) * len(key)) / 2) != 0:
        number_of_tables += 1
    list_of_table = []
    for i in range(number_of_tables):
        list_of_table.append(copy.deepcopy(table))
    number_word_letter = 0
    for tab in range(len(list_of_table)):
        for row in range(len(list_of_table[tab])):
            for col in range(len(list_of_table[tab][row])):
                if list_of_table[tab][row][col] == '\u0000':
                    if number_word_letter == len(word):
                        break
                    else:
                        list_of_table[tab][row][col] = word[number_word_letter]
                        number_word_letter += 1
    encrypted = ''

    _n = int(max(order))
    for tab in range(len(list_of_table)):
        for col in range(_n + 1):
            for row in range(_n + 1):
                encrypted += list_of_table[tab][row][col]

    return encrypted


def decrypt(word, key):
    return "None"


def __str__():
    return "Matrix C"


def main():
    word = "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION"
    key = "CONVENIENCE"
    print(encrypt(word, key))
    pasw = decrypt(encrypt(word, key), key)
    print(pasw)
    print(word == pasw)


if __name__ == '__main__':
    main()
