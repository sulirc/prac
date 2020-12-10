from os import sys

class StrKeyDict0(dict):
    def __missing__(self, key):
        
        if isinstance(key, str):
            raise KeyError(key)

        return self[str[key]]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


obj = StrKeyDict0({"name": "ygj"})
print(obj.get("name", "suli"))
print(obj.get("age", 25))

    
