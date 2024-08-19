import re
from glycobase import structure


class automaton:
    states = ["name", "value", "range"]
    matcher = {
        "name": r"^\d+\s+(\w+)",
        "value": r"^\d+(\.\d+)?(\s*±\s*\d*(\.\d+)?)?",
        "range": r"^\d+\.\d+-\d+\.\d+",
    }

    def __init__(self):
        self.init_state()

    def dispatch(self, line: str):

        if self.state < 3 and re.match(self.matcher[self.states[self.state]], line):
            self.state += 1
            self.recognized.append(line)
            return True
        if self.state < 2:
            raise ValueError(
                "Invalid line format "
                + line
                + " expected: "
                + self.matcher[self.states[self.state]]
            )
        return False

    def get_structure(self):
        struct = structure(
            self.recognized[0],
            self.recognized[1],
            self.recognized[2].split("-") if len(self.recognized) > 2 else None,
        )
        self.init_state()
        return struct

    def init_state(self):
        self.state = 0
        self.recognized = []


def reorganize_csv(file_name, output_file=None):
    parser = automaton()

    with open(file_name, "r") as file:
        lines = file.readlines()
    line_no = 0
    structures = []
    for line in lines:
        line_no += 1
        try:
            line = line.strip()
            if line == "" or parser.dispatch(line):
                continue
            structures.append(parser.get_structure())
            parser.dispatch(line)
        except ValueError as e:
            print(f"Error at line {line_no}: {e}")
            return None
    if output_file:
        with open(output_file, "w") as file:
            for struct in structures:
                file.write(str(struct) + "\n")

    return structures
