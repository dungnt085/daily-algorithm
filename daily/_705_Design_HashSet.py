class MyHashSet(object):

    def __init__(self):
        self.values = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.values:
            self.values.add(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.values:
            self.values.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.values:
            return True
        else:
            return False

my_hash_set = MyHashSet()
print(my_hash_set.values)
my_hash_set.add(1)
print(my_hash_set.values)

my_hash_set.add(2)
print(my_hash_set.values)

my_hash_set.remove(2)
print(my_hash_set.values)