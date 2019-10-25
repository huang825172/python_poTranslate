# 用于处理字符串中特殊符号部分和自然语言部分的 合并和拼接
class Instance:
    def __init__(self):
        self._elem = []
        self._map = []

    # 以一个 task_pack 进行初始化，包括一个 字符串序列（由一行分割而来），以及一个 与序列相同长度的 map 序列
    # map 序列的元素只有 0 或者 1，如果序号为 idx 的 map 元素为 1，表示序号为 idx 的 elem 元素为特殊符号，不需要翻译
    def init(self, pack):
        self._elem = pack[0]
        self._map = pack[1]

    # 返回一个合并后的未翻译字符串列表（排除特殊符号）
    def get_not_translated(self):
        list = []
        str = ""
        for idx in range(len(self._elem)):
            if self._map[idx] == 1:
                if len(str) > 0:
                    list.append(str)
                str = ""
            else:
                if len(str) > 0:
                    str += " "
                str += self._elem[idx]
        if len(str) > 0:
            list.append(str)
        return list

    # 设置与未翻译字符串列表同样长的翻译后字符串列表
    # 用于生成翻译结果字符串列表（包括特殊符号）
    def set_translated(self, list):
        new_list = []
        if len(list) != len(self.get_not_translated()):
            raise RuntimeError("List length not match!")
        idx = 0
        pointer = 0
        while idx < len(self._elem):
            if self._map[idx] == 1:
                new_list.append(self._elem[idx] + " ")
                idx += 1
            else:
                new_list.append(list[pointer] + " ")
                while idx < len(self._elem) and self._map[idx] == 0:
                    idx += 1
                pointer += 1
        return new_list

    def print_raw(self):
        print(self._elem, self._map)
