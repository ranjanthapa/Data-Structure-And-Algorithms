class HashTable:
    def __init__(self):
        self.maxSize = 10
        self.data = [[] for i in range(self.maxSize)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.maxSize

    def __setitem__(self, key, val):
        address = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.data[address]):

            if len(element) == 2 and element[0] == key:
                self.data[address][idx] = (key, val)
                found = True
        if not found:
            self.data[address].append((key, val))

    def __getitem__(self, key):
        address = self.get_hash(key)
        for element in self.data[address]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        address = self.get_hash(key)
        for idx, val in enumerate(self.data[address]):
            if val[0] == key:
                print("delete", idx)
                del self.data[address][idx]


if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 63457
    print(t["march 17"])

    print(t.data)
    del t["march 17"]
    print(t.data)
