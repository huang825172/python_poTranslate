from potranslator import translator

if __name__ == "__main__":
    translator.translate("wedevs-project-manager-zh_CN.po")
    translator.translate("ultimate-member-zh_CN.po")
    # 调用 potranslator 包进行翻译工作，默认输出文件 translated_FILENAME.po
    # 以后考虑实现命令行接口或者 GUI 接口