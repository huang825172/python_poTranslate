import re


# po文件读入器
class Instance:
    def __init__(self, filename):
        self._fileName = filename
        self._fileRaw = ""
        self._fileStruct = []
        self.META_LABEL = "META"
        self.TASK_LABEL = "TASK"
        self.init()

    # 读入一个文件，返回一个 po文件数据结构
    # 文件数据分为两种，一种是不需要改动的 META 数据段，另一种是包含 msgid msgstr 对的 TASK 数据段
    def init(self):
        with open(self._fileName, 'r', encoding="UTF-8") as poFile:
            self._fileRaw = poFile.readlines()
        if len(self._fileRaw) < 1:
            raise FileNotFoundError("File not found or empty: {}".format(self._fileName))
        pattern = re.compile('(?<=\")(.+?)(?=\")')
        idx = 0
        while idx < len(self._fileRaw):
            line = self._fileRaw[idx]
            if line.find("msgid") == -1:
                self._fileStruct.append((self.META_LABEL, self._fileRaw[idx]))
                idx += 1
                continue
            else:
                msgididx = idx
                tasklines = []
                while self._fileRaw[msgididx].find("msgstr") == -1:
                    match_raw = pattern.search(self._fileRaw[msgididx])
                    taskline = (match_raw.group() if match_raw is not None else '')
                    tasklines.append(taskline)
                    msgididx += 1
                match_raw = pattern.search(self._fileRaw[msgididx])
                strline = (match_raw.group() if match_raw is not None else '')
                tasklines.append(strline)
                self._fileStruct.append((self.TASK_LABEL, tasklines))
                idx = msgididx + 1

    def get_filestruct(self):
        return self._fileStruct

    def print_raw(self):
        print(self._fileRaw)
