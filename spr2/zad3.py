import string

def check_params(arg1, arg2):
    if(len(arg2) == len(arg1)):
        return True
    else:
        return False

def correct_value(value):
    while value.startswith("0"):
        value = value[1:]
    value = list(map(int, value)) #convert string list to int list
    return value

def create_shift_table(degree):
    table = [""] * (degree+1)

    for row in range(degree+1):
        table[row] = [""] * (degree)

    return table


x = '1000'
x = correct_value(x)

polynomial = "0001011" # (x^4 + x^2 + x^1)
last_index_1_value = polynomial.rfind("1")
first_index_1_value = polynomial.find("1")

polynomial = correct_value(polynomial)

polynomial_degree = len(polynomial)

shift_table = create_shift_table(polynomial_degree)

polynomial_array = polynomial

reversed_polynomial_array = polynomial_array[::-1]

if(check_params(x, polynomial)):

    significent_value = polynomial_degree - (last_index_1_value-first_index_1_value)

    for row in range(polynomial_degree + 1):
        xor_sum = 0
        for col in range(polynomial_degree):
            if row == 0: # First row
                shift_table[row] = polynomial_array
                break
            else: #Every row despite first one
                if (reversed_polynomial_array[col] == 1):
                    xor_sum += shift_table[row - 1][col]

                if col > 0:
                    shift_table[row][col] = shift_table[row - 1][col - 1]
                    if col == ( polynomial_degree - 1): #Last column in every row
                        xor_sum += x[row-1]
                        shift_table[row][0] = xor_sum % 2
    print(shift_table)