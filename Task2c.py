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
                if number_word_letter<len(word):
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
    decrypted = ''
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

    #Uzupelnianie tabeli

    #ilosc wierszy zapisanych w ostatniej tabeli.
    rows_in_last_table = 0
    max_col_in_last_table = 0
    letters_in_last_table = word_length % number_word_in_table
    letters_in_last_row = 0

    for row_in_last_table in range(N):
        if letters_in_last_table > 0:
            letters_in_last_row = 0
            for col_in_last_table in range(N):
                if(order.index(row_in_last_table) >= order.index(col_in_last_table) and letters_in_last_table > 0):
                    letters_in_last_row += 1
                    letters_in_last_table -= 1
                    if(col_in_last_table >= max_col_in_last_table):
                        max_col_in_last_table = col_in_last_table
            rows_in_last_table += 1

    counter = 0

    for col_index in range(N):
        order_index = order.index(col_index)
        for tab_index in range(number_of_tables):
            for row_index in range(N):
                if(order.index(row_index) >= order_index and counter < len(word) and (tab_index != number_of_tables-1 or rows_in_last_table == 0)):
                    list_of_table[tab_index][row_index][order_index] = word[counter]
                    counter += 1
                if tab_index == (number_of_tables - 1):
                    #if(row_index < rows_in_last_table and row_index < order.index(max_col_in_last_table) and counter < len(word) and order_index <= max_col_in_last_table):
                    if(row_index != rows_in_last_table - 1):
                        if(row_index < rows_in_last_table and order.index(row_index) >= order_index and counter < len(word) and order_index <= max_col_in_last_table):
                            list_of_table[tab_index][row_index][order_index] = word[counter]
                            counter += 1
                    elif (letters_in_last_row > order.index(col_index)):
                        list_of_table[tab_index][row_index][order_index] = word[counter]
                        counter += 1


    #Zliczam ilosc zapisanych linii

    for tab_index in range(number_of_tables):
        for row_index in range(N):
            for col_index in range(N):
                decrypted += list_of_table[tab_index][row_index][col_index]

    return decrypted

def __str__():
    return "Matrix C"

def main():

    print(encrypt('KOTOLAKI_BRAKIMOWIC', 'KOTOLAKI'))
    print(encrypt('HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION', 'CONVENIENCE'))
    print(encrypt('ALA_MA_KOTA_ACO', 'ALA'))
    print(encrypt('ALA_MA_KOTA_DOSI', 'ALA'))
    print(encrypt('ALA_MA_KOTA_DOSIE_POD_KOCEM_ANTKA', 'BA'))
    print('-----------')

    print(decrypt('AAIKKMOKLROIWOBCT_I', 'KOTOLAKI'))
    print(decrypt('LMKAOEOKEAKAA_A_OT_DSI_PD_OCM_NTA', 'BA'))
    print(decrypt('ALM_KAAC_TAAO_O','ALA'))
    print(decrypt('HEESPNIRRSSEESEIYASCBTEMGEPNANDICTRTAHSOIEERO','CONVENIENCE'))
    print(decrypt('ALM_KADO_TIAAO_S','ALA'))
    '''
    word = "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION"
    key = "CONVENIENCE"
    print(encrypt(word, key))
    pasw = decrypt(encrypt(word, key), key)
    print(pasw)
    print(word == pasw)
    '''
if __name__ == '__main__':
    main()
