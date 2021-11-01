storage = [None] * 10
s1 = "BCA"
s2 = "CAB"
s3 = "ABC"



# def my_hashing_func(str):
#     bytes_representation = str.encode()

#     sum = 0
#     for byte in bytes_representation:
#         sum += byte

#     return sum

def my_hashing_func(str, table_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % table_size

def put(key, val):
  index = my_hashing_func(key, 10)
  storage[index] = val

def get(key):
  index = my_hashing_func(key, 10)
  return storage[index]



# print(my_hashing_func(s1, len(storage)))
# print(my_hashing_func(s2, len(storage)))
# print(my_hashing_func(s3, len(storage)))

put("Murray", 12345)
put("rayMur", 54321)
print(get("Murray"))