from libpo import reader as libpo_reader
from libpo import filter as libpo_filter
from libpo import connector as libpo_connector
from libbdtranslate import bdapi

META_LABEL = "META"
TASK_LABEL = "TASK"


def translate(filename):
    try:
        po_reader = libpo_reader.Instance(filename)
        po_filter = libpo_filter.Instance()
        po_connector = libpo_connector.Instance()
        po_writer = open("out.po", 'w', encoding='UTF-8')
        po_bdapi = bdapi.Instance()
        for part in po_reader.get_filestruct():
            if part[0] == META_LABEL:
                po_writer.write(part[1])
            elif part[0] == TASK_LABEL:
                if len(part[1][-1]) > 0:
                    po_writer.write("msgid ")
                    for idx in range(len(part[1]) - 1):
                        po_writer.write('"{}"\n'.format(part[1][idx]))
                    po_writer.write('msgstr "{}"\n'.format(part[1][-1]))
                else:
                    po_writer.write("msgid ")
                    for idx in range(len(part[1]) - 1):
                        po_writer.write('"{}"\n'.format(part[1][idx]))
                        # po_writer.write(str(po_connector.get_not_translated()))
                        # po_connector.print_raw()
                        # print(po_connector.set_translated(["任务标记为", "在里面"]))
                    po_writer.write('msgstr ')
                    for idx in range(len(part[1]) - 1):
                        po_filter.init(part[1][idx])
                        po_filter.process()
                        po_connector.init(po_filter.get_pack())
                        trans_list = po_connector.get_not_translated()
                        transed_list = []
                        for trans_word in trans_list:
                            transed_list.append(po_bdapi.translate(trans_word))
                        transed_line = po_connector.set_translated(transed_list)
                        transed_str = ''
                        for word in transed_line:
                            transed_str += (word+' ')
                        po_writer.write('"{}"\n'.format(transed_str))
        po_writer.close()
    except FileNotFoundError as e:
        print(e)
        exit(0)
    except RuntimeError as e:
        print(e)
        exit(0)
