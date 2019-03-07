import math


def create_order(key):
    key_split = []
    key_split[:0] = key

    key_position = [['\u0000'] * len(key)]

    position = 0

    for i in range(ord('A'), ord('Z')):
        for index in range(len(key)):
            if ord(key_split[index]) == i:
                key_position[0][index] = position
                position += 1
    return key_position


def encrypt(word, key):
    table = []
    encrypted = ''
    row_max = math.ceil(len(word) / len(key))
    for level in range(row_max):
        table.append(['\u0000'] * len(key))

    col_max = len(key)
    index_max = len(word)
    index = 0

    for row in range(row_max):
        for col in range(col_max):
            if not (index == index_max):
                table[row][col] = word[index]
                index += 1

    order = create_order(key)

    for i in range(len(order[0])):
        for j in range(len(order[0])):
            if order[0][j] == i:
                for k in range(row_max):
                    if not table[k][j] == '\u0000':
                        encrypted += table[k][j]
    print("Encrypted: " + encrypted)
    return encrypted


def decrypt(word, key):
    table = []
    decrypted = ""
    row_max = math.ceil(len(word) / len(key))
    row_min = row_max - 1
    for level in range(row_max):
        table.append(['\u0000'] * len(key))

    dif = len(word) % len(key)
    counter = row_max

    order = create_order(key)

    col_index = 0
    print("------")

    count_min_word = 0
    count_max_word = 0
    for j in range(len(order[0])):
        if order[0][j] < dif:
            start_spliting_index = (count_min_word * (row_max - 1) + count_max_word * row_max)
            splited_word = word[start_spliting_index:(start_spliting_index + counter)]

            for k in range(row_max):
                table[k][order[0].index(col_index)] = splited_word[k]

            count_max_word += 1
            col_index += 1

        elif order[0][j] >= dif:
            start_spliting_index = (count_min_word * (row_max - 1) + count_max_word * row_max)
            splited_word = word[start_spliting_index:(start_spliting_index + counter)]

            for k in range(row_min):
                table[k][order[0].index(col_index)] = splited_word[k]
            count_min_word += 1
            col_index += 1

    for row in range(row_max):
        decrypted += ''.join(table[row])

    decrypted = decrypted.replace("\u0000", "")
    print("Decrypted: " + decrypted)
    return decrypted


def __str__():
    return "Matrix B"

# def main():
#     print("\nMessage: " + "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITIONS " + "\nKEY: " + "CONVENIENCE")
#     print("------")
#
#     encrypt("HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITIONS", "CONVENIENCE")
#     decrypt("HECRNCEYIISEPSGDIRNTOAAESRMPNSSROEEBTETIASEEHS", "CONVENIENCE")
#
#
# if __name__ == '__main__':
#     main()
