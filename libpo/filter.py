import re


class Instance:
    def __init__(self):
        self.line = []
        self.map = []

    def init(self, line):
        self.line = []
        self.map = []
        self.line = line.split()
        for _ in self.line:
            self.map.append(0)

    def process(self):
        for idx in range(len(self.line)):
            if self.line[idx].find('<') != -1 \
                    or self.line[idx].find('>') != -1 \
                    or self.line[idx].find('\\') != -1 \
                    or self.line[idx].find('%') != -1 \
                    or self.line[idx].find('[') != -1:
                self.map[idx] = 1

    def get_pack(self):
        return self.line, self.map

    def print_element(self):
        print(self.get_pack())
