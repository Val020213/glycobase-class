from glycobase import structure, read_glycobase
from reorganize import reorganize_csv


def testing():
    print("Hello, World!")
    reorganize_csv("./docs/tmp.csv", "./docs/glycobase_data.csv")
    data = read_glycobase("./docs/glycobase_data.csv")
    for d in data:
        print(d)


if __name__ == "__main__":

    testing()
