import dill
import os
import sys


class Dumper:
    def __init__(self):
        if not os.path.exists("cache_glycobase"):
            os.makedirs("cache_glycobase")
        pass

    def save_object(self, object, object_name):
        sys.setrecursionlimit(10000)
        if not os.path.exists(object_name):
            os.makedirs(object_name)
        with open(f"./cache_glycobase/{object_name}.plk", "wb") as file_pkl:
            dill.dump(object, file_pkl)

    def load_object(self, object_name):
        if not os.path.exists(object_name):
            raise FileNotFoundError(f"File {object_name} not found")
        with open(f"./cache_glycobase/{object_name}.plk", "rb") as file_pkl:
            return dill.load(file_pkl)
