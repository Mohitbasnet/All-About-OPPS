# Q-6: FlexibleDict
# As of now we are accessing values from dictionary with exact keys. Now we want to amend accessing values functionality. if a dict have key 1 (int) the even if we try to access values by giving '1' (1 as str) as key, we should get the same result and vice versa.

# Write a class FlexibleDict upon builtin dict class with above required functionality.

# Hint- dict[key] => dict.__getitem__(key)

class FlexibleDict(dict):
    def __getitem__(self, key):
        # Convert the key to integer if it's a string and exists in the dictionary
        if isinstance(key, str) and key.isdigit() and int(key) in self:
            key = int(key)
        # Convert the key to string if it's an integer and exists in the dictionary
        elif isinstance(key, int) and str(key) in self:
            key = str(key)
        return super().__getitem__(key)

# Example usage:
fd = FlexibleDict({1: 'value1', '2': 'value2', 3: 'value3'})

# Access values using integers or strings
print(fd[1])   # Output: value1
print(fd['1']) # Output: value1
print(fd[2])   # Output: value2
print(fd['2']) # Output: value2
print(fd[3])   # Output: value3
print(fd['3']) # Output: value3
