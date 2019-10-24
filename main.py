from poReader import reader
from poReader import filter
from poReader import connector

if __name__ == "__main__":
    try:
        reader = reader.Instance("wedevs-project-manager-zh_CN.po")

        filter = filter.Instance()
        connector = connector.Instance()
        for item in reader.notTranslated:
            print(item[0])
            filter.init(item[0])
            filter.process()
            connector.init(filter.get_pack())
            connector.print_raw()
            print(connector.set_translated(["任务标记为", "在里面"]))
            break
    except FileNotFoundError as e:
        print(e)
        exit(0)
    except RuntimeError as e:
        print(e)
        exit(0)
