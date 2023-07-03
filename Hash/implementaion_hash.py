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
            print(element)
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

    def keys(self):
        if len(self.data) == 0:
            return None
        key_array = []
        for i in range(0, len(self.data)):

            if self.data[i]:
                if len(self.data[i]) < 1:
                    key_array.append(self.data[i][0][0])

                for j in range(0, len(self.data[i])):
                    key_array.append(self.data[i][j][0])
        return key_array


if __name__ == '__main__':
    t = HashTable()
    t["Grapes"] = 230
    t["Apple"] = 230
    t["Mango"] = 180
    print(t.data)
    print(t.keys())
