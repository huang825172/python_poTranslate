class Instance:
    def __init__(self):
        pass

    # 临时的 fake translator，此处需要加入对 百度翻译API 的 restful 调用
    # 此函数的功能是将 word 翻译成中文，以字符串形式返回
    # 修改功能后，需要去掉静态方法修饰器
    @staticmethod
    def translate(word):
        return "中文"
