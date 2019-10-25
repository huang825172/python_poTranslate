# 用于对特殊符号进行过滤处理
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

    # 生成 task_pack 的代码，filter 的核心
    # 经过一晚上的思考感觉这玩意太碎了
    # 实在不行跑个模型吧
    # task_pack 详细定义见 connector 注释
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
