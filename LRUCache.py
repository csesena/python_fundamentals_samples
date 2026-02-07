class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        value = self.cache.pop(key, -1)
        if (value != -1):
            self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if (key in self.cache):
            del self.cache[key]
        self.cache[key] = value
        if (self.capacity < len(self.cache)):
            del self.cache[next(iter(self.cache))]
        print (self.cache)

""" lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print (lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print (lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print (lRUCache.get(1))    # return -1 (not found)
print (lRUCache.get(3))    # return 3
print (lRUCache.get(4))    # return 4 """

lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 3)
lRUCache.put(4, 1)
print (lRUCache.get(1))
print (lRUCache.get(2))