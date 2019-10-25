import libbdtranslate.bdapi as bdapi
from libpo import filter as libpo_filter
from libpo import connector as libpo_connector


# 用于对翻译任务块进行翻译工作的 task_translate
class Instance:
    def __init__(self):
        self._task_list = []
        self._out_list = []
        self._filter = libpo_filter.Instance()
        self._connector = libpo_connector.Instance()
        self._translate_api = bdapi.Instance("appid", "key")
        self._translate_api.translatew("apple", "en", "zh")

    # 对一个未翻译字符串列表初始化
    def init(self, task_list):
        self._out_list = []
        self._task_list = task_list

    # 调用 bdapi 包进行翻译工作，返回相应长度的翻译后字符串列表
    def do_translate(self):
        for task in self._task_list:
            if len(task) == 0:
                self._out_list.append('')
            else:
                self._filter.init(task)
                self._filter.process()
                self._connector.init(self._filter.get_pack())
                not_translated = self._connector.get_not_translated()
                translated = []
                for item in not_translated:
                    translated.append(self._translate_api.translate(item))
                translated_line = self._connector.set_translated(translated)
                translated_str = ''
                for item in translated_line:
                    translated_str += (item + ' ')
                self._out_list.append(translated_str)

    def get_output(self):
        return self._out_list
