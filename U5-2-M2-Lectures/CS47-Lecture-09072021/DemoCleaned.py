"""
Your task is create your own HashTable without using a built-in library.
Your HashTable needs to have the following functions:
- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.
"""
# [8][ABC, 1]->[CBA, 45]->[BAC, 10]->None

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.storage = [None] * self.size

    def my_hashing_func(self, str):
        bytes_representation = str.encode()
        sum = 0
        for byte in bytes_representation:
            sum += byte
        return sum % self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        index = self.my_hashing_func(key)
        if self.storage[index] == None:
            self.storage[index] = ListNode(key, value)
        else:
            current = self.storage[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next == None:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.my_hashing_func(key)
        current = self.storage[index]
        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping 
        for the key
        """
        index = self.my_hashing_func(key)
        current = self.storage[index]
        prev = self.storage[index]
        if current == None:
            return
        if current.key == key:
            self.storage[index] = current.next
        else:
            current = current.next
            while current:
                if current.key == key:
                    prev.next == current.next
                    break
                else:
                    prev = prev.next
                    current = current.next

# tests
hash_table = MyHashTable()
hash_table.put("a", 1)  # ht["a"] = 1
hash_table.put("b", 2)
print(hash_table.get("a"))            # returns 1
print(hash_table.get("c"))            # returns -1 (not found)
hash_table.put("b", 1)         # update the existing value
print(hash_table.get("b"))            # returns 1
hash_table.remove("b")         # remove the mapping for 2
print(hash_table.get("b"))            # returns -1 (not found)
