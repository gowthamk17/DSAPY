class HashMap():
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def __get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, value):
        h = self.__get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))       

    def __getitem__(self, key):
        h = self.__get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.__get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


if __name__ == "__main__":
    hMap = HashMap()
    hMap["march"] = 2345
    hMap["mardg"] = 5674
    print(hMap["march"])
    del hMap["mardg"]
    print(hMap["mardg"])