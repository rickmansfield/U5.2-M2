# Unit 5.2 M2 Task 3
What is the most common strategy for dealing with hash collisions?

The most common strategy for dealing with hash collisions is not storing the values directly at an index of the hash table's array. Instead, the array index stores a pointer to a linked list. Each node in the linked list stores a key, value, and a pointer to the next item in the linked list.