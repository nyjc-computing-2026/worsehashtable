def _hash_key(key: str, p: int = 53, m: int = 10**9 + 9) -> int:
    """Hashes the key using the rolling polynomial algorithm.

    Arguments:
    - key: str
      The key to be hashed.
    - p: int
      A prime number used for the rolling polynomial algorithm

    Returns:
    - the hashed location (int)
    """
    total = 0
    for i, char in enumerate(key):
        total += ord(char) * p**i
    return total % m



class HashTable:
    """A hashtable without collision resolution.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with

    Attributes:
    - size: int
      The number of slots that the hash table has
    - length: int
      The number of records contained in the hash table
    """

    def __init__(self, size: int):
        self.size = size
        self.length = 0
        self._arr = [None] * size

    def __repr__(self) -> str:
        return f"HashTable(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        key_hash = _hash_key(key)
        index = key_hash % self.size
        if self._arr[index] == None:
            self.length += 1   
        self._arr[index] = value

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        key_hash = _hash_key(key)
        index = key_hash % self.size
        if self._arr[index] == None:
            raise KeyError("key does not exist")
        return self._arr[index]

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        key_hash = _hash_key(key)
        index = key_hash % self.size
        value = self._arr[index]
        if not value:
            raise KeyError("key does not exist")
        self._arr[index] = None
        self.length -= 1


class HashTableLinearProbing(HashTable):
    """
    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        #key -> (key,value)
        key_hash = _hash_key(key)
        init_index = key_hash % self.size
        index = (init_index + 1) % self.size
        while (init_index != index):
            if self._arr[index] == None:
                self.length += 1
                self._arr[index] = (key, value)
                return None
            elif self._arr[index][0] == key:
                self._arr[index] = (key, value)
                return None
            index = (index + 1) % self.size
        raise MemoryError("hash table is full")
        
    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        # key_hash = _hash_key(key)
        # index = key_hash % self.size
        # while (self._arr[index] != None and self._arr[index][0] != key and index != self.size):
        #     index = (index + 1) % self.size
        # if self._arr[index] == None:
        #     raise KeyError("key does not exist")
        # return self._arr[index][1]
    
        key_hash = _hash_key(key)
        init_index = key_hash % self.size
        index = (init_index + 1) % self.size
        while (init_index != index):
            if self._arr[index] == None:
                raise KeyError("key does not exist")
            if self._arr[index][0] == key:
                return self._arr[index][1]
            index = (index + 1) % self.size
        raise KeyError("key does not exist")

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        # key_hash = _hash_key(key)
        # index = key_hash % self.size
        # while (self._arr[index] != None and self._arr[index][0] != key and index != self.size):
        #     index = (index + 1) % self.size
        # if self._arr[index] == None:
        #     raise KeyError("Key does not exist")
        # self.length -= 1
        # self._arr[index] = None
        # index += 1
        # while _hash_key(self._arr[index][0]) == key_hash:
        #     self._arr[index-1] = self._arr[index]
        #     index += 1
        key_hash = _hash_key(key)
        init_index = key_hash % self.size
        index = (init_index + 1) % self.size
        while (init_index != index):
            if self._arr[index] != None and self._arr[index][0] == key:
                self._arr[index] = None
                self.length -= 1
                return None
            index = (index + 1) % self.size
        raise KeyError("key does not exist")


class HashTableSeparateChaining(HashTable):
    """A hashtable that implements collision resolution using
    separate chaining.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        raise NotImplementedError

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError
