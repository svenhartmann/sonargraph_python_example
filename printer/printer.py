class Printer(object):
    def __init__(self, obj):
        self.obj = obj

    def print(self):
        print(self.obj)

class PrintXmlHelper(Printer):
    def print(self):
        print('<person><name>' + str(self.obj) + '</name></person>')