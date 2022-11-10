class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arry = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arry[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arry[h] is None:
            self.arry[h] = (key,val)
        else:
            new_h = self.find_slot(key,h)
            self.arry[new_h] = (key,val)
            print(self.arry)

    def get_prob_range(self,index):
        return [*range(index,len(self.arry))]+[*range(0,index)]

    def find_slot(self,key,index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arry[prob_index] is None:
                return prob_index
            if self.arry[prob_index][0] == key:
                return prob_index
            raise Exception("Hashmap is full")