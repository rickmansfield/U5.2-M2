"""
Modify the function below to use a different procedure for generating a hash. Research some other basic methods ("mid-squares", "division hashing", "multiplicative hashing", etc.) for ideas.

"""
example_string = "hello"

def my_hashing_func(str, table_size):
    bytes_representation = str.encode()
    # print(bytes_representation)

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % table_size

print(my_hashing_func(example_string, 10))