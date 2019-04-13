from bitarray import bitarray


# The same as bitarray(), but support bits shifting
class OwnBitarray(bitarray):

    def __lshift__(self, count):
        end = self[:count]
        return self[count:] + end

    def __rshift__(self, count):
        start = self[count:]
        return start + self[:-count]

    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, self.to01())

    # def addown(self, other):
    #    return type(self)('') *
