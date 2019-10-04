#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        
        Average Case: O(n * l) == O(n*2), where n is the number of bucket and l is the length of ll in each bucket. 
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        
        Average Case: O(n * l) == O(n*2), where n is the number of bucket and l is the length of ll in each bucket. 
        """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                values.append(value)
        return values


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        
        Best Case: O(n). If only each ll have 1 or less element each.
        Average Case: O(n * l). We are iterating through each bucket. Extend() then iterate over its argument and adding each element in the ll
        to the new list.
        """
        # Collect all pairs of key-value entries in each bucket

        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?
        
        Best Case: O(n). If only each ll have 1 or less element each. Len() will be O(1)
        Average Case: O(n * l). We are iterating through each bucket. Extend() then iterate over its argument and adding each element in the ll
        to the new list. Len() will be O(1)
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        return len(self.items())

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?
        
        Best case: O(1) if the item is at the head of the ll inside hash bucket
        Worst case: O(n) if the item is not at the head or does not exist.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        item = bucket.find(lambda x: x[0] == key)

        if item:
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        
        Best case: O(1) if the item is at the head of the ll inside hash bucket
        Worst case: O(n) if the item is not at the head or does not exist.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        item = bucket.find(lambda x: x[0] == key)

        if item is not None:
            return item[1]
        raise KeyError('Key not found: {}'.format(key))


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?
        
        Best case: O(1) if the item exist and is at the head of bucket.
        Worst case: O(n) if the item is not at the head or does not exist.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        index = self._bucket_index(key)
        bucket = self.buckets[index]

        try:
            self.delete(key)
        except KeyError:
            pass
        
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        
        Best case: O(1) if the item exist and is at the head of bucket.
        Worst case: O(n) if the item is not at the head or does not exist
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        item = bucket.find(lambda x: x[0] == key)

        if item:
            bucket.delete(item)
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
