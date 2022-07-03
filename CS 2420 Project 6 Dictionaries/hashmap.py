class HashMap:
    def __init__(self):
        self.entries = 0
        self.buckets = 7
        self.lyst = [[(None, None)] for _ in range(self.buckets)]

    def hsh(self, tup):
        return (tup[0] * tup[1]) % self.buckets

    def get(self, key):
        return self.__getitem__(key)

    def __getitem__(self, key):
        key_i = self.lyst[self.hsh(key)]
        for _ in key_i:
            for j in key_i:
                if j[0] == key:
                    return j[1]
        raise KeyError

    def set(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        hashed = self.hsh(key)
        if self.lyst[hashed][0][0] is None:
            self.lyst[hashed] = [(key, value)]
            self.entries += 1
        elif self.lyst[hashed][0][0] == key:
            self.lyst[hashed][0] = (key, value)
        else:
            self.lyst[hashed].append((key, value))
            self.entries += 1
        if self.entries / self.buckets >= .8:
            temp = self.lyst
            self.buckets = (self.buckets * 2) - 1
            self.entries = 0
            self.lyst = [[(None, None)] for _ in range(self.buckets)]
            for i in temp:
                for j in i:
                    if j[0] is not None:
                        self[j[0]] = j[1]

    def remove(self, key):
        hashed = self.hsh(key)
        key_i = self.lyst[hashed]
        for i in key_i:
            if i[0] == key:
                if len(key_i) == 1:
                    self.lyst[hashed] = [(None, None)]
                else:
                    self.lyst[hashed].remove(self.lyst[hashed][key_i.index(i)])

    def clear(self):
        """
        Clears the list and resets the buckets and entries to default values
        """
        self.entries = 0
        self.buckets = 7
        self.lyst = [[(None, None)] for _ in range(self.buckets)]

    def capacity(self):
        return self.buckets

    def size(self):
        return self.entries

    def keys(self):
        """
        :return: A list of all keys
        """
        key_list = []
        for i in self.lyst:
            for j in i:
                if j[0] is not None:
                    key_list.append(j[0])
        return key_list
