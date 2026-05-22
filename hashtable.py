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
                # reinsert new hashes
                return None
            index = (index + 1) % self.size
        raise KeyError("key does not exist")

class Node():
    """
    A node, which is used to store a key-value pair, as well as the next node.

    Attributes:
    key (str): the key of the tuple
    value (dict): the value of the tuple
    next (node): the next node, or None if there is none after
    """
    def __init__(self, key: str, value: dict) -> None:
        self.key = key
        self.value = value
        self.next = None

class LinkedList():
    """
    A Linked List, consisting of nodes dynamically allocated and linked.

    Attributes:
    head (node): the first node in the list, or None if it is empty.
    """
    
    def __init__(self):
        self.head = None

    def getkey(self, key: str) -> dict:
        """
        Returns the value associated with the key in a Linked List.

        Arguments:
        key (str): the key to search for

        Returns:
        value (dict): the value in the key-value pair

        Raises:
        KeyError if key does not exist, or list is empty
        """
        if self.head == None:
            raise KeyError("list is empty")
        current_node = self.head
        while (current_node != None):
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        raise KeyError("key does not exist")
    
    def setitem(self, key: str, value: dict) -> None:
        """
        Sets the value in the Linked List with same key to the specified value.
        If the key does not exist, creates a new Node to store the key-value pair.

        Arguments:
        key (str): the key of the key-value pair
        value (dict): the value of the key-value pair
        """
        new_node = Node(key, value)
        if self.head == None:  # empty list
            self.head = new_node
            return None
        if self.head.key == key:  # first item is replaced
            new_node.next = self.head.next  # links to rest of list
            self.head = new_node
            return None
        current_node = self.head
        while current_node != None:  # repeats until end
            if current_node.key == key:  # replace this one
                new_node.next = current_node.next
                prev_node.next = new_node
                return None
            prev_node = current_node
            current_node = current_node.next
        # when current_node is None, prev_node is last item
        prev_node.next = new_node
        return None
    
    def delkey(self, key: str) -> None:
        """
        Deletes Node in Linked List with key.
        
        Arguments:
        key (str): the key to be deleted

        Raises:
        KeyError if key not found, or list is empty
        """
        if self.head == None:
            return KeyError("list is empty")
        if self.head.key == key:  # delete at start
            self.head = self.head.next
            return None
        current_node = self.head.next
        prev_node = self.head
        while (current_node != None):
            if current_node.key == key:
                prev_node.next = current_node.next
                return None
            current_node = current_node.next
            prev_node = prev_node.next
        # not found
        raise KeyError("key not found")

class HashTableSeparateChaining(HashTable):
    """A hashtable that implements collision resolution using
    separate chaining.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        for i in range(self.size):
            self._arr[i] = LinkedList()

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        index = _hash_key(key) % self.size
        self._arr[index].setitem(key, value)

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key) % self.size
        return self._arr[index].getkey(key)

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key) % self.size
        self._arr[index].delkey(key)
