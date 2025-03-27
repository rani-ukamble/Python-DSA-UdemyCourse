class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None]*size 
    
    def _hash(self, key):
        myhash = 0
        for letter in key:
            myhash = (myhash + ord(letter)*23) % len(self.data_map)
        return myhash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] 
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None 
    
    def keys(self):
        allKeys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    allKeys.append(self.data_map[i][j][0])
        return allKeys
    

myhashtable = HashTable()

myhashtable.set_item('bolts', 1400)
myhashtable.set_item('washers', 50)
myhashtable.set_item('lumber', 70)

# print(myhashtable.get_item('bolts'))
# print(myhashtable.get_item('washers'))

# myhashtable.print_table()
print(myhashtable.keys())