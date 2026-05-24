class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.li = [[] for _ in range(1000)]

    def _hash_key(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash_key(key)
        idx = -1
        for i in range(len(self.li[hash_key])):
            if self.li[hash_key][i][0] == key:
               idx = i
               break
        if idx == -1:
            self.li[hash_key].append((key, value))
        else:
            self.li[hash_key][idx] = (key, value)

    def get(self, key: int) -> int:
        hash_key = self._hash_key(key)
        if self.li[hash_key]:
            for i in range(len(self.li[hash_key])):
                if self.li[hash_key][i][0] == key:
                    return self.li[hash_key][i][1]
        
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._hash_key(key)
        if self.li[hash_key]:
            for i in range(len(self.li[hash_key])):
                if self.li[hash_key][i][0] == key:
                    self.li[hash_key][-1], self.li[hash_key][i] = self.li[hash_key][i], self.li[hash_key][-1]
                    break
        
            if self.li[hash_key][-1][0] == key:
                self.li[hash_key].pop()


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)