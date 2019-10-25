import re


class Instance:
    def __init__(self):
        self._line = []
        self._map = []

    def init(self, line):
        self._line = []
        self._map = []
        self._line = line.split()
        for _ in self._line:
            self._map.append(0)

    def process(self):
        for idx in range(len(self._line)):
            if self._line[idx].find('<') != -1 \
                    or self._line[idx].find('>') != -1 \
                    or self._line[idx].find('\\') != -1 \
                    or self._line[idx].find('%') != -1 \
                    or self._line[idx].find('[') != -1:
                self._map[idx] = 1

    def get_pack(self):
        return self._line, self._map

    def print_element(self):
        print(self.get_pack())
