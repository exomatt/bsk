def encrypt(word, sequence):
    table = []
    encrypted = ''
    size = int(len(word) / len(sequence) + 1)
    for level in range(size):
        table.append(['\u0000'] * len(sequence))

    char_number = 0
    for row in range(len(table)):
        for col in range(len(sequence)):
            if char_number == len(word):
                break
            table[row][col] = word[char_number]
            char_number += 1
    for row in range(len(table)):
        for sequence_number in range(len(table[0])):
            if table[row][sequence[sequence_number] - 1] == '\u0000':
                continue
            encrypted += table[row][sequence[sequence_number] - 1]
    return encrypted


def main():
    print(encrypt("ALA_MA_KOTA", [4, 3, 1, 2]))


if __name__ == '__main__':
    main()
