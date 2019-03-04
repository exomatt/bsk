def encrypt(levels, word):
    table = []
    encrypted = ''
    for level in range(levels):
        table.append(['\u0000'] * len(word))

    level_number = 0
    column_number = 0
    direction = False  # false down true up
    for letter_position in range(len(word)):
        if level_number == 0:
            direction = not direction
        if level_number == levels - 1:
            direction = not direction

        table[level_number][column_number] = word[letter_position]
        column_number += 1
        if direction:
            level_number = level_number + 1
        else:
            level_number = level_number - 1

    for row in table:
        for cell in row:
            encrypted += cell

    return encrypted.replace("\u0000", "")


def decrypt(levels, word):
    table = []
    decrypted = ''
    direction = False
    level_number = 0
    column_number = 0

    for level in range(levels):
        table.append(['\u0000'] * len(word))

    for letter_position in range(len(word)):
        if level_number == 0:
            direction = not direction

        if level_number == levels - 1:
            direction = not direction

        table[level_number][column_number] = word[letter_position]
        column_number += 1

        if direction:
            level_number = level_number + 1
        else:
            level_number = level_number - 1

    char_number = 0
    new_table = []

    for level in range(levels):
        new_table.append(['\u0000'] * len(word))

    for row in range(len(table)):
        for cell in range(len(word)):
            if (table[row][cell] != '\u0000') and (char_number < len(word)):
                new_table[row][cell] = word[char_number]
                char_number += 1

    level_number = 0
    column_number = 0

    for letter_position in range(len(word)):
        if level_number == 0:
            direction = not direction

        if level_number == levels - 1:
            direction = not direction

        if new_table[level_number][column_number] != '\u0000':
            decrypted += new_table[level_number][column_number]
            column_number += 1

        if direction:
            level_number = level_number + 1
        else:
            level_number = level_number - 1

    return decrypted


def main():
    print(encrypt(4, "ALA_MA_KOTA"))
    decrypt(4, "A_LAKAMOA_T")


if __name__ == '__main__':
    main()
