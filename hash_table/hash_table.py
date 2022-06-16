# We'll start creating a list with a fixed size
MAX_HASH_TABLE_SIZE = 4096
data_list = [None] * 4096
print("Data list has lenght of 4096:", len(data_list) == MAX_HASH_TABLE_SIZE)

# Hashing Function
# Used to convert non-numeric data types into numbers which can be used as list indices.
# Example: if the hash function converts "Aakash" into 4, then the key-value pair ("Aakash", 123456) will be stored at index 4 inside a list.

# A simple algorithm for hashing, which can convert strings into numeric list indices:
# 1. Iterate over the string, character by character
# 2. Convert each character to a number using Python's built-in ord function.
# 3. Add the numbers for each character to obtain the hash for the entire string
# 4. Take the remainder of the result with the size of the data list

def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0
    
    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number
    
    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

print("The index of 'Aakash' is 585:", get_index(data_list, 'Aakash') == 585)

# INSERT: Get the hash of the key and store the key-value pair in that index
key, value = "Aakash", "123456"
idx = get_index(data_list, key)
data_list[idx] = (key, value)
print("---- INSERT ----")
print("Index where key-value pair will be inserted:", idx)
print("Now", data_list[idx], "is stored at index", idx)

# FIND: Get the hash of the key and search the returned index in the list
print("---- FIND ----")
print("Get index of 'Aakash':", idx)
print("Value of 'Aakash':", data_list[idx][1])

# LIST: List the keys using 'list comprehension'
keys_list = [x[0] for x in data_list if x is not None]
print("List all keys:", keys_list)

# Basic Hash Table
class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value
    
    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]

# Handling collisions with Linear Probing
# A collision is when multiple keys have the same hash. A solution for this is using "Linear Probing":
#
# 1. While INSERTING a new key-value pair if the target index for a key is occupied by another key, then we try the next index,
#    followed by the next and so on until finding the closest empty location.
#
# 2. While FINDING a key-value pair, we apply the same strategy, but instead of searching for an empty location,
#    we look for a location which contains a key-value pair with the matching key.
#
# 3. While UPDATING a key-value pair, we apply the same strategy, but instead of searching for an empty location,
#    we look for a location which contains a key-value pair with the matching key, and update its value.

# Hash Table with Linear Probing

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if kv[0] == key:
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
     
    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value
    
    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
    
    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]