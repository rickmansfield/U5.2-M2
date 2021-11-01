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
        # logic to deal with collisions
        # if there is nothing in the storage at the current index
        if self.storage[index] == None:
            # instantiate a new ListNode with a key value pair from the passed in key and value
            # place the new ListNode in to the storage at the current index
            self.storage[index] = ListNode(key, value)
        # otherwise
        else:
            # traverse the linked list
            # get the current node from the storage at the current index
            current = self.storage[index]
            # while True
            while True:
                # check if the current nodes key is equal to the passed in key
                if current.key == key:
                    # set the current nodes value to the passed in value
                    current.value = value
                    # return
                    return
                # if the current nodes next is None
                if current.next == None:
                    # break out of the loop
                    break
                # traverse to the next node
                current = current.next

            # create a new ListNode with the given key and value
            # place the new list node in to the storage at the current.next position
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.my_hashing_func(key)
        # traversal of a linked list
        # get the current node of the linked list
        current = self.storage[index]
        # while current node
        while current:
            # check if the current node key is equal the the passed in key
            if current.key == key:
                # return current nodes value
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

        # keep track of current and prev node
        current = self.storage[index]
        prev = self.storage[index]

        # if the current is None
        if current == None:
            # return from the method
            return

        # if the current nodes key is equal to the passed in key
        if current.key == key:
            # set the storage at the current index to the current nodes next
            self.storage[index] = current.next

        # otherwise
        else:
            # traverse to the next node
            current = current.next

            # while current
            while current:
                # check if the current nodes key is equal to the passed in key
                if current.key == key:
                    # set the prev nodes next to the current nodes next
                    prev.next == current.next
                    # break
                    break
                # otherwise
                else:
                    # set prev to prex.next
                    prev = prev.next
                    # set current to current.next
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
