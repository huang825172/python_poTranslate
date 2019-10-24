import re


class Instance:
    def __init__(self, filename):
        self._fileName = filename
        self._fileRaw = ""
        self._filePairs = []
        self.notTranslated = []
        self.Translated = []
        self.init()

    def init(self):
        with open(self._fileName, 'r', encoding="UTF-8") as poFile:
            self._fileRaw = poFile.readlines()
        if len(self._fileRaw) < 1:
            raise FileNotFoundError("File not found or empty: {}".format(self._fileName))
        pattern = re.compile('(?<=\")(.+?)(?=\")')
        for index in range(len(self._fileRaw)):
            if self._fileRaw[index].find("msgid") != -1:
                if self._fileRaw[index + 1].find("msgstr") != -1:
                    msgid_raw = pattern.search(self._fileRaw[index].strip())
                    msgstr_raw = pattern.search(self._fileRaw[index + 1].strip())
                    msgid = (msgid_raw.group() if msgid_raw is not None else "")
                    msgstr = (msgstr_raw.group() if msgstr_raw is not None else "")
                    if msgid == '' or msgstr == '':
                        if msgid == '' and msgstr == '':
                            continue
                        else:
                            self.notTranslated.append((msgid, msgstr))
                    else:
                        self.Translated.append((msgid, msgstr))

    def print_raw(self):
        print(self._fileRaw)

    def print_not_translated(self):
        print(self.notTranslated)
