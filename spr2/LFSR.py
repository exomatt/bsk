import array


class LFSR:
    def __init__(self):
        with open("test.txt", "w") as f:
            f.write('')
        self.seed = 0
        self.output = 0
        self.polynomial = None
        self.arr = None
        self.poly = None

    def lfsr(self, seed, polynomial, n):
        if polynomial.endswith('0'):
            return "Polynomial starts with 0"
        if len(seed) != len(polynomial):
            return "Params arent the same length"
        self.arr = array.array('i', (0 for i in range(0, len(seed))))
        self.poly = array.array('i', (0 for i in range(0, len(seed))))
        # out = array.array('i', (0 for i in range(0, int(n))))
        for i in range(0, len(seed)):
            self.arr[i] = int(seed[i])
            self.poly[i] = int(polynomial[i])
        print(self.arr)
        print(self.poly)

        # with open("test.txt", "w") as f:
        #     for i in range(0, int(n)):
        #         for j in range(len(seed) - 1, 0, -1):
        #             arr[j] = arr[j - 1]
        #         self.output = arr[len(polynomial) - 1]
        #         for j in range(len(polynomial) - 2, 0, -1):
        #             if poly[j] == 1:
        #                 self.output = (self.output + arr[j]) % 2
        #         arr[0] = self.output
        #         f.write(', '.join(str(x) for x in arr))
        #         f.write('\n')
        # return arr[0]

    def next(self):
        if self.poly is None or self.arr is None:
            return
        temp = self.arr[:]
        for j in range(len(self.arr) - 1, 0, -1):
            self.arr[j] = self.arr[j - 1]
        self.output = self.arr[len(self.poly) - 1]
        for j in range(len(self.poly) - 1, 0, -1):
            if self.poly[j - 1] == 1:
                self.output = (self.output + self.arr[j - 1]) % 2
        self.arr[0] = self.output
        with open("test.txt", "a+") as f:
            f.write(', '.join(str(x) for x in self.arr))
            f.write('\n')
        return self.arr[0]


def main():
    print("Main")
    obj = LFSR()
    obj.lfsr("10110", "10011", "24")

    for i in range(0, 24):
        x = obj.next()
        if x is None:
            return
        print(x)

    # counter=0
    # with open("test.bin", "rb") as f:
    #     byte = f.read(1)
    # print(counter)


if __name__ == '__main__':
    main()
