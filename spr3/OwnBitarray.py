from bitarray import bitarray

# The same as bitarray(), but support bits shifting
class OwnBitarray(bitarray):

    def __lshift__(self, count):
        return self[count:] + type(self)('0') * count

    def __rshift__(self, count):
        return type(self)('0') * count + self[:-count]

    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, self.to01())

    # def addown(self, other):
