import string


def check_params(arg1, arg2):
    if (len(arg2) == len(arg1)):
        return True
    else:
        return False


def correct_value(value):
    while value.startswith("0"):
        value = value[1:]
    value = list(map(int, value))  # convert string list to int list
    return value


def create_shift_table(x_degree, polynomial_degree):
    table = [""] * (x_degree + 1)

    for row in range(x_degree + 1):
        table[row] = [""] * polynomial_degree

    return table


def encrypt(polynomial, x):
    x = correct_value(x)

    last_index_1_value = polynomial.rfind("1")

    first_index_1_value = polynomial.find("1")

    polynomial = correct_value(polynomial)  # (x^4 + x^2 + x^1)

    polynomial_degree = len(polynomial)
    x_degree = len(x)

    shift_table = create_shift_table(x_degree, polynomial_degree)

    polynomial_array = polynomial

    reversed_polynomial_array = polynomial_array[::-1]

    significent_value = polynomial_degree - (last_index_1_value - first_index_1_value)

    for row in range(x_degree + 1):
        xor_sum = 0
        for col in range(polynomial_degree):
            if row == 0:  # First row
                shift_table[row] = polynomial_array
                break
            else:  # Every row despite first one
                if reversed_polynomial_array[col] == 1:
                    xor_sum += shift_table[row - 1][col]

                if col > 0:
                    shift_table[row][col] = shift_table[row - 1][col - 1]
                    if col == (polynomial_degree - 1):  # Last column in every row
                        xor_sum += x[row - 1]
                        shift_table[row][0] = xor_sum % 2
    print(shift_table)

    key = ""
    for row in range(x_degree):
        key = int(str(key) + str(shift_table[row + 1][significent_value - 1]))

    print('Y=' + str(key))


def decrypt(polynomial, y):
    y = correct_value(y)

    last_index_1_value = polynomial.rfind("1")

    first_index_1_value = polynomial.find("1")

    polynomial = correct_value(polynomial)  # (x^4 + x^2 + x^1)

    polynomial_degree = len(polynomial)
    y_degree = len(y)

    shift_table = create_shift_table(y_degree, polynomial_degree)

    polynomial_array = polynomial

    reversed_polynomial_array = polynomial_array[::-1]

    for row in range(y_degree + 1):
        for col in range(polynomial_degree):
            if row == 0:  # First row
                shift_table[row] = polynomial_array
                break
            else:  # For every row
                if col == 0:
                    shift_table[row][col] = y[row - 1]
                elif col > 0:
                    shift_table[row][col] = shift_table[row - 1][col - 1]
    x = ''
    print(shift_table)
    for row in range(y_degree):
        value = 0
        for col in range(polynomial_degree):
            if reversed_polynomial_array[col] == 1:
                value += shift_table[row][col]
        value += y[row]

        value = value % 2

        x = int(str(x) + str(value))

    print('X=' + str(x))


def main():
    encrypt('1011', '1000')  # Y = 1100
    decrypt('1011', '1100')


if __name__ == '__main__':
    main()
