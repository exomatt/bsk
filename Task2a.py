def check_param(sequence):
    sequence = sequence.split('-')
    _sum = 0
    _pow = 0
    for i in range(len(sequence)):
        sequence[i] = int(sequence[i])
        _sum += sequence[i]
        _pow += (i + 1)
    if _sum != _pow:
        return False
    return sequence


def check_for_spaces(word):
    i = 0
    while i < (len(word)):
        if word[i] == ' ':
            word = word[:i] + word[(i + 1):]
        else:
            i += 1
    return word


def encrypt(word, sequence):
    word = check_for_spaces(word)
    table = []
    encrypted = ''
    try:
        sequence = check_param(sequence)
        if not sequence:
            return "Elements of sequence don't add up"
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
    except ValueError:
        return "Wrong value entered"


def decrypt(word, sequence):
    encrypted = '0' * (len(word))
    sequence = check_param(sequence)
    if not sequence:
        return "Elements of sequence don't add up"
    temp = 0
    while len(word) > 0:
        for i in range(len(sequence)):
            if len(word) > 0:
                val = (sequence[i] - 1) + temp * (len(sequence))
                if val < len(encrypted):
                    x = list(encrypted)
                    x[val] = word[0]
                    encrypted = "".join(x)
                    word = word[1:]
        temp += 1
    return encrypted


def __str__():
    return "Matrix A"


def main():
    key = "2-4-1-3"
    word = "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITIONS"
    print(encrypt(word, key))
    pasw = decrypt(encrypt(word, key), key)
    print(pasw)
    print(word == pasw)


if __name__ == '__main__':
    main()
