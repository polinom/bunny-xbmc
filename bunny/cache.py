# simple cache implementation
import time


class Cache(object):
    def __init__(self, expires_in=0):
        self.expires_in = expires_in
        self._cache = {}
        self._key_time = {}
        self.key_order = {}


    def set(self,key,value):
        self.clear_expired()
        self._cache[key] = value
        self._key_time[key] = int(time.time()) + self.expires_in


    def get(self, key):
        self.clear_expired()
        return self._cache.get(key)


    def clear_expired(self):
        t = int(time.time())
        for key, value in self._key_time.items():
            if value < t:
                self.delete(key)


    def delete(self,key):
        del self._cache[key]
        del self._key_time[key]