
from typing import List, Any

class HashTable:
    def __init__(self, size: int):
        """Initialize the hash table with given size.
        Args:
            size: The size of the hash table.
        """
        # TODO: Implement __init__
        # 1. Set the size attribute
        # 2. Initialize the table as a list with None values of length size
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: Any) -> int:
        """Compute the hash value for a given key.
        Args:
            key: The key to hash.
        Returns:
            Hash value as an integer.
        """
        # TODO: Implement hash_function
        # 1. Compute the hash value using hash() and modulo with size
        # 2. Return the computed hash value
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        """Insert a key-value pair into the hash table.
        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        # TODO: Implement insert
        # 1. Compute the hash index using hash_function
        # 2. Check if the position at index is None, insert if so
        # 3. If there is a collision, handle it (e.g., by linear probing)
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key: Any) -> Any:
        """Search for the value associated with a key in the hash table.
        Args:
            key: The key to search for.
        Returns:
            The value associated with the key, or None if not found.
        """
        # TODO: Implement search
        # 1. Compute the hash index using hash_function
        # 2. Loop to find the key, handling collisions
        # 3. Return the value if found, otherwise None
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                return None
        return None

if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert("apple", 100)
    hash_table.insert("banana", 200)
    hash_table.insert("orange", 300)
    print(hash_table.search("apple"))
    print(hash_table.search("banana"))
    print(hash_table.search("orange"))
    print(hash_table.search("grape"))
