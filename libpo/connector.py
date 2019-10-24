class Instance:
    def __init__(self):
        self.elem = []
        self.map = []

    def init(self, pack):
        self.elem = pack[0]
        self.map = pack[1]

    def get_not_translated(self):
        list = []
        str = ""
        for idx in range(len(self.elem)):
            if self.map[idx] == 1:
                if len(str) > 0:
                    list.append(str)
                str = ""
            else:
                if len(str) > 0:
                    str += " "
                str += self.elem[idx]
        if len(str) > 0:
            list.append(str)
        return list

    def set_translated(self, list):
        new_list = []
        if len(list) != len(self.get_not_translated()):
            raise RuntimeError("List length not match!")
        idx = 0
        pointer = 0
        while idx < len(self.elem):
            if self.map[idx] == 1:
                new_list.append(self.elem[idx]+" ")
                idx += 1
            else:
                new_list.append(list[pointer]+" ")
                while idx<len(self.elem) and self.map[idx] == 0:
                    idx += 1
                pointer += 1
        return new_list

    def print_raw(self):
        print(self.elem, self.map)
