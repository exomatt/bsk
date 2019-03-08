def encrypt(word, key):
    encrypted = ''
    key = int(key)
    for level in range(key):
        pos = level
        encrypted += word[pos]
        while True:
            leap = 2 * (key - 1) - 2 * level
            if leap != 0:
                pos += leap
                if pos >= len(word):
                    break
                encrypted += word[pos]

            leap = 2 * (key - 1) - 2 * (key - 1 - level)
            if leap > 0:
                pos += leap
                if pos >= len(word):
                    break
                encrypted += word[pos]
    return encrypted


def decrypt(word, key):
    key = int(key)
    encrypted = '0' * len(word)
    for level in range(key):
        pos = level
        temp = list(encrypted)
        temp[pos] = word[0]
        encrypted = "".join(temp)
        if len(word) > 0:
            word = word[1:]
        while True:
            leap = 2 * (key - 1) - 2 * level
            if leap != 0:
                pos += leap
                if pos >= len(encrypted):
                    break
                temp = list(encrypted)
                temp[pos] = word[0]
                encrypted = "".join(temp)
                if len(word) > 0:
                    word = word[1:]

            leap = 2 * (key - 1) - 2 * (key - 1 - level)
            if leap > 0:
                pos += leap
                if pos >= len(encrypted):
                    break
                temp = list(encrypted)
                temp[pos] = word[0]
                encrypted = "".join(temp)
                if len(word) > 0:
                    word = word[1:]
    return encrypted


def __str__():
    return "Railfence"


def main():
    key = "4"
    word = "ALA_MA_KOTA"
    print(encrypt(word, key))
    pasw = decrypt(encrypt(word, key), key)
    print(pasw)
    print(word == pasw)


if __name__ == '__main__':
    main()
