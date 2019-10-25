import libbdtranslate.bdapi as bdapi
from libpo import filter as libpo_filter
from libpo import connector as libpo_connector


class Instance():
    def __init__(self):
        self._task_list = []
        self._out_list = []
        self._filter = libpo_filter.Instance()
        self._connector = libpo_connector.Instance()
        self._translate_api = bdapi.Instance()

    def init(self, task_list):
        self._out_list = []
        self._task_list = task_list

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
