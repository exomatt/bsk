import math
import string, copy


def p(item):
    print("-----")
    print(item)
    print("-----")


def encrypt(word, key):
    alphabet = string.ascii_uppercase
    order = []
    number = 0
    encrypted = ''
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

    word_length = len(word)
    N = max(order) + 1
    number_word_in_table = ((1 + (max(order)+1))*len(key))/2 #Maximum amount of letters in table NxN -> S(n) =(S(1)+S(N)*N)/2

    number_of_tables = math.ceil(word_length / number_word_in_table)

    list_of_table = []
    for i in range(number_of_tables):
        list_of_table.append(copy.deepcopy(table))

    number_word_letter = 0

    for tab in range(len(list_of_table)):
        counter = 0
        for row in range(len(list_of_table[tab])):
            index_to_skip = order.index(counter)
            for col in range(index_to_skip + 1):
                if  number_word_letter<len(word):
                    list_of_table[tab][row][col] = word[number_word_letter]
                    number_word_letter += 1
            counter += 1

    for col_index in range(N):
        order_index = order.index(col_index)
        for tab_index in range(number_of_tables):
            for row_index in range(N):
                encrypted += list_of_table[tab_index][row_index][order_index]

    return encrypted

def decrypt(word, key):
    alphabet = string.ascii_uppercase
    order = []
    number = 0
    encrypted = ''
    for i in range(len(key)):
        order.append("")
    for char in alphabet:
        for letter_number in range(len(key)):
            if char == key[letter_number]:
                order[letter_number] = number
                number += 1

    table = [""] * len(key)

    word_length = len(word)
    N = max(order) + 1
    number_word_in_table = ((1 + (max(order) + 1)) * len(key)) / 2  # Maximum amount of letters in table NxN -> S(n) =(S(1)+S(N)*N)/2

    number_of_tables = math.ceil(word_length / number_word_in_table)

    list_of_table = []
    for i in range(number_of_tables):
        list_of_table.append(copy.deepcopy(table))

    number_word_letter = 0





    for row in range(len(table)):
        table[row] = [""] * len(key)




def main():
     print(encrypt('ALA_MA_KOTA_DOSIE_POD_KOCEM_ANTKA', 'BA'))

if __name__ == '__main__':
    main()
