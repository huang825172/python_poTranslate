from libpo import reader as libpo_reader
from libbdtranslate import task_translate

META_LABEL = "META"
TASK_LABEL = "TASK"


def translate(filename):
    try:
        po_reader = libpo_reader.Instance(filename)
        po_writer = open("out.po", 'w', encoding='UTF-8')
        po_translator = task_translate.Instance()
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
                    po_writer.write('msgstr ')
                    po_translator.init(part[1][:-1])
                    po_translator.do_translate()
                    transed_line = po_translator.get_output()
                    for line in transed_line:
                        po_writer.write('"{}"\n'.format(line))
        po_writer.close()
    except FileNotFoundError as e:
        print(e)
        exit(0)
    except RuntimeError as e:
        print(e)
        exit(0)
