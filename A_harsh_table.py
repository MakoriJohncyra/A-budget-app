class HashTable:
    def __init__(self):
        """Initialize the hash table with an empty collection dictionary"""
        self.collection = {}
    
    def hash(self, key):
        """
        Compute hash value by summing Unicode values of each character in the key
        """
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value
    
    def add(self, key, value):
        """
        Add a key-value pair to the hash table
        If multiple keys hash to the same value, store them in a nested dictionary
        """
        hashed_key = self.hash(key)
        
        # If this hash value doesn't exist yet, create a new dictionary
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        
        # Store the key-value pair under the hashed key
        self.collection[hashed_key][key] = value
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table
        If the key doesn't exist, do nothing (no error)
        """
        hashed_key = self.hash(key)
        
        # Check if the hashed key exists in collection
        if hashed_key in self.collection:
            # Check if the specific key exists in the nested dictionary
            if key in self.collection[hashed_key]:
                # Remove the key-value pair
                del self.collection[hashed_key][key]
                
                # If the nested dictionary becomes empty, remove it
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]
    
    def lookup(self, key):
        """
        Look up a key and return its corresponding value
        Returns None if the key doesn't exist
        """
        hashed_key = self.hash(key)
        
        # Check if the hashed key exists
        if hashed_key in self.collection:
            # Check if the specific key exists in the nested dictionary
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        
        # Key not found
        return None
    
    def __str__(self):
        """String representation of the hash table for debugging"""
        return str(self.collection)


# Example usage and testing
if __name__ == "__main__":
    # Create a new hash table
    ht = HashTable()
    
    # Test adding key-value pairs
    ht.add("name", "John")
    ht.add("age", 25)
    ht.add("city", "New York")
    
    # Test lookup
    print(ht.lookup("name"))  # Should print: John
    print(ht.lookup("age"))   # Should print: 25
    print(ht.lookup("city"))  # Should print: New York
    print(ht.lookup("country"))  # Should print: None
    
    # Test hash collisions (keys that sum to same Unicode value)
    # Note: "abc" and "cba" will have different hash values due to different order
    # Let's find two strings that actually collide
    # For demonstration, we'll use "abc" (ord('a')+ord('b')+ord('c') = 97+98+99 = 294)
    # and "bac" (ord('b')+ord('a')+ord('c') = 98+97+99 = 294) - these actually sum to same value!
    ht.add("abc", "first value")
    ht.add("bac", "second value")
    
    # Both should be stored under the same hash (294)
    print("\nAfter adding colliding keys:")
    print(f"Hash of 'abc': {ht.hash('abc')}")  # 294
    print(f"Hash of 'bac': {ht.hash('bac')}")  # 294
    print(f"Collection: {ht}")
    
    # Look up both values
    print(f"Lookup 'abc': {ht.lookup('abc')}")  # first value
    print(f"Lookup 'bac': {ht.lookup('bac')}")  # second value
    
    # Test removal
    ht.remove("age")
    print(f"\nAfter removing 'age':")
    print(f"Lookup 'age': {ht.lookup('age')}")  # None
    
    # Test removing non-existent key (should not error)
    ht.remove("nonexistent")
    print(f"After removing non-existent key (no error): {ht}")
    
    # Test removing all keys from a hash bucket
    ht.remove("abc")
    ht.remove("bac")
    print(f"After removing both colliding keys: {ht}")
