class HashMap():
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def __get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, value):
        h = self.__get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.__get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.__get_hash(key)
        self.arr[h] = None


if __name__ == "__main__":
    hm = HashMap()
    hm["user1"] = 2345
    hm["user2"] = 5674
    print(hm["user1"])
    del hm["user1"]
    print(hm["user1"])
