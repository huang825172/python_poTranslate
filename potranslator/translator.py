from libpo import reader as libpo_reader
from libbdtranslate import task_translate

META_LABEL = "META"
TASK_LABEL = "TASK"

# 对指定文件进行翻译工作
# 暂时没有实现多线程
# 考虑到百度翻译的效率，后续可能需要实现异步调用和线程同步
def translate(filename):
    try:
        po_reader = libpo_reader.Instance(filename)
        po_writer = open("translated_" + filename, 'w', encoding='UTF-8')
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
    except RuntimeError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        if po_writer:
            po_writer.close()
