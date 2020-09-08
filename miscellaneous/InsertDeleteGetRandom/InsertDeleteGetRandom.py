class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        new_val = True
        if val in self.dict:
            new_val = False
        self.arr.append(val)
        if new_val:
            self.dict[val] = {len(self.arr)-1}
        else:
            self.dict[val].add(len(self.arr)-1)
        return new_val

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.dict:
            return False
        popped_index = self.dict[val].pop()
        if len(self.dict[val])==0:
            del self.dict[val]
        if popped_index == len(self.arr)-1: #we happened to already pick the last val in the array
            self.arr.pop()
        else:
            last_elem_in_arr = self.arr[-1]
            self.dict[last_elem_in_arr].remove(len(self.arr)-1)
            self.dict[last_elem_in_arr].add(popped_index)
            self.arr[popped_index] = self.arr[-1]
            self.arr.pop()
        return True
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()