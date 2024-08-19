from typing import Union
from dumper import Dumper


class structure:
    def __init__(self, name: str, value: str, range: Union[float, float] = None):
        self.name = name
        self.value = value
        self.range = range if range else [float(value), float(value)]

    def __str__(self):
        return f"{self.name}; {self.value}; {self.range[0]}-{self.range[1]}"

    @staticmethod
    def read(line: str):
        line = line.strip()
        name, value, my_range = line.split(";")
        my_range = my_range.split("-")
        my_range = [float(my_range[0]), float(my_range[1])]
        return structure(name, value, my_range)


def read_glycobase(file_name="./docs/glycobase_data.csv"):
    dmp = Dumper()
    data = []
    try:
        data = dmp.load_object("glycobase_data")
    except FileNotFoundError:
        with open(file_name, "r") as file:
            lines = file.readlines()
        data = [structure.read(line) for line in lines if line.strip() != ""]
        dmp.save_object(data, "glycobase_data")
    return data
